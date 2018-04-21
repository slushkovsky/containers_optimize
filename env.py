import json

import redis

from frontend.app import REDIS_KEY


class Container(object):
    def __init__(self, id: int, server: int =None):
        self.id = id
        self.server = server

    def change_server(self, new_server: int) -> None:
        # Here will be container move login
        self.server = new_server

class Env(object):
    metrics = ('CPU', 'RAM', 'Trafic')

    def __init__(self, servers_count: int, containers_count: int):
        self.servers_count = servers_count
        self.containers = [Container(id=i) for i in range(containers_count)]
        
        self.states_count = len(self.metrics) * servers_count
        self.actions_count = servers_count * containers_count

    def reset(self):
        pass

    def step(self, action):
        pass

    def _make_action(self, action):
        pass

    def _dump_to_redis(self):
        r = redis.StrictRedis()
        r.set(REDIS_KEY, json.dumps({
            'servers_count': self.servers_count,
            'containers': [
                {
                    'id': container.id,
                    'server': container.server
                } for container in self.containers
            ]
        }).encode())
