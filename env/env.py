import json
import random

import redis

#import frontend.app
from .utils import Resources
from .server import Server
from .container import Container
from .state import State
from .log import logger


class Env(object):
    def __init__(self, servers_count: int, containers_count: int):
        logger.info(f'Initilizing environment (servers count: {servers_count}, containers count: {containers_count})')

        self.servers_count = servers_count
        self.servers = [Server.random_aws_instance() for _ in range(servers_count)]
        self.containers = [Container.create_random() for _ in range(containers_count)]
        
        self.state_size = State.get_state_len(containers_count)

        self.__actions = []
        
        for container_idx in range(containers_count):
            for server_idx in range(servers_count):
                self.__actions.append(lambda : self.containers[container_idx].change_server(server_idx))

        self.actions_count = len(self.__actions)

    def to_dict(self):
        return {
            'servers_count': self.servers_count,
            'servers': [server.to_dict() for server in self.servers],
            'containers': [container.to_dict() for container in self.containers]
        }

    def reset(self):
        for container in self.containers:
            container.change_server(random.randint(0, self.servers_count))

        self.step_num = 0

        logger.debug('Environment reseted')

        return State(self.containers, self.step_num)

    def step(self, action: int):
        was_moved = self.__actions[action]()
        reward = self.__get_step_reward(was_moved)

        logger.info(f'Environment step {self.step_num} done, reward={reward} (action={action})')
        
        self.step_num += 1

        new_state = State(self.containers, self.step_num)

        return new_state, reward

    def __get_step_reward(self, was_container_move: bool):
        overloads = [server.calc_overload(self.__server_sum_demands(server.id)) for server in self.servers]

        debuff = 0

        for cpu, ram, traffic in overloads:
            logger.debug(f'Server overload: {cpu} CPU, {ram} RAM, {traffic} traffic')
            debuff += int(cpu) + int(ram) + int(traffic)

        reward =  1 - was_container_move - debuff
        logger.debug(f'Reward calc: {reward} = 1 - was_container_move({was_container_move}) - debuff({debuff})')

        return reward

    def __server_sum_demands(self, server_id: int) -> Resources:
        resources = [container.demands.on_step(self.step_num) for container in self.containers if container.server_id == server_id]
        return sum(resources, Resources())

    # def dump_to_redis(self, key=frontend.app.REDIS_KEY):
    def dump_to_redis(self, key='data'):
        redis.StrictRedis().set(key, json.dumps(self.to_dict()).encode())
