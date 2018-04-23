import random
import math


class RPSNature(object):
    FUNCS = {
        'y = |sin x| * x': lambda t: abs(math.sin(t/10)) * t,
        'y = x':           lambda t: t,
        'y = x^2':         lambda t: t**2
    }

    def __init__(self, func, factor, max_value, func_name=''):
        self.func = func
        self.factor = factor
        self.max_value = max_value
        self.func_name = func_name

    def __repr__(self):
        return f'<RPSPolicy (func="{self.func_name}", factor={self.factor}, max_value={self.max_value})'

    def to_dict(self):
        return {
            'func': self.func_name,
            'factor': self.factor,
            'max_value': self.max_value
        }

    @classmethod
    def create_random(cls):
        func_name = random.choice(list(cls.FUNCS.keys()))

        return cls(
            func=cls.FUNCS[func_name],
            factor=random.randint(1, 1e2),
            max_value=random.randint(1e1, 1e5),
            func_name=func_name
        )

    def on_step(self, step: int):
        return min(self.func(step) * self.factor, self.max_value)

