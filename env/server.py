import random
import json

from utils import Resources


class Server(object):
    def __init__(self, id, resources: Resources, name=''):
        self.resources = resources
        self.name = name
        self.id = id

    def __repr__(self):
        return f'<Server {self.name} (cpu: {self.resources.cpu}, ram: {self.resources.ram}, bandwidth: {self.resources.traffic})>'

    def to_dict(self):
        return {
            'name': self.name,
            'resources': self.resources.to_dict()
        }

    @classmethod
    def create(cls, *args, **kw):
        cretaed_count = getattr(cls, '__created_count', 0)
        cretaed_count += 1
        setattr(cls, '__cretaed_count', cretaed_count)
        return cls(cretaed_count, *args, **kw)

    @classmethod
    def random_aws_instance(cls, instances_file='aws_instances.json'):
        with open(instances_file) as f:
            instances = json.load(f)

        name = random.choice(list(instances.keys()))
        instance = instances[name]

        return cls.create(Resources(cpu=instance['cpu_count'], ram=instance['ram'], traffic=instance['bandwidth']), name=name)

    def calc_overload(self, sum_demands: Resources):
        return sum_demands.cpu / self.resources.cpu, sum_demands.ram / self.resources.ram, sum_demands.traffic / self.resources.traffic
