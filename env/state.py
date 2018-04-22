from container import Container


class State(list):
    def __init__(self, containers: Container, step: int):
        for container in containers:
            demands = container.demands.on_step(step)
            self.append(container.server_id)
            self.append(demands.cpu)
            self.append(demands.ram)
            self.append(demands.traffic) 

    @staticmethod
    def get_state_len(containers_count):
        return 4 * containers_count
