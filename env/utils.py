class Resources(object):
    def __init__(self, cpu: float = .0, ram: float = .0, traffic: float = .0):
        self.cpu = cpu
        self.ram = ram
        self.traffic = traffic

    def __repr__(self):
        return f'<Resources (cpu={round(self.cpu, 2)}, ram={round(self.ram, 2)}, traffic={round(self.traffic, 2)}>'

    def __add__(self, other):
        self.cpu += other.cpu
        self.ram += other.ram
        self.traffic += other.traffic

        return self

    def to_dict(self):
        return {
            'cpu': self.cpu,
            'ram': self.ram,
            'traffic': self.traffic
        }
