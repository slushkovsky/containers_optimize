import random

from utils import Resources
from rps_nature import RPSNature


class ContainerDemands(object):
    def __init__(self, cpu_base: float, cpu_per_request: float, ram_base: float, ram_per_request: float, traffic_per_request: float, rps_nature: RPSNature):
        self.cpu_base = cpu_base
        self.cpu_per_request = cpu_per_request
        self.ram_base = ram_base
        self.ram_per_request = ram_per_request
        self.traffic_per_request = traffic_per_request
        self.rps_nature = rps_nature

    @classmethod
    def create_random(cls):
        return cls(
            cpu_base=random.uniform(1e-2, 1e-4),
            cpu_per_request=random.uniform(1e-3, 1e-5),
            ram_base=random.uniform(1e-1, 1e-2),
            ram_per_request=random.uniform(1e-3, 1e-5),
            traffic_per_request=random.uniform(1e-3, 1e-5),
            rps_nature = RPSNature.create_random()
        )

    def to_dict(self):
        return {
            'cpu': {
                'base': self.cpu_base,
                'per_request': self.cpu_per_request
            },
            'ram': {
                'base': self.ram_base,
                'per_reeuqest': self.ram_per_request
            },
            'traffic': {
                'per_request': self.traffic_per_request
            },
            'rps_nature': self.rps_nature.to_dict()
        }

    def on_step(self, step: int):
        rps = self.rps_nature.on_step(step)

        return Resources(
            cpu=self.cpu_base + self.cpu_per_request * rps,
            ram=self.ram_base + self.ram_per_request * rps,
            traffic=self.traffic_per_request * rps
        )

class Container(object):
    def __init__(self, id: int, demands: ContainerDemands, server_id: int = None):
        self.id = id
        self.server_id = server_id
        self.demands = demands

    def __repr__(self):
        return f'<Container {self.id} (on server: {self.server_id})>'

    def to_dict(self):
        return {
            'id': self.id,
            'server_id': self.server_id,
            'demands': self.demands.to_dict(),
        }

    @classmethod
    def create(cls, *args, **kw):
        created_count = getattr(cls, '__created_count', 0)
        created_count += 1
        setattr(cls, '__created_count', created_count)
        return cls(created_count, *args, **kw)

    @classmethod
    def create_random(cls):
        return cls.create(demands=ContainerDemands.create_random())

    def change_server(self, new_server_id: int) -> None:
        if self.server_id == new_server_id:
            return False

        # Here will be container move login
        
        self.server_id = new_server_id

        return True
