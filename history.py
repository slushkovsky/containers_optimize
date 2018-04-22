import numpy as np


class HistoryItem(object):
    def __init__(self, state, action, step_reward, new_state):
        self.state = state
        self.action = action
        self.step_reward = step_reward
        self.new_state = new_state

class History(list):
    def add(self, state, action, step_reward, new_state):
        self.append(HistoryItem(state, action, step_reward, new_state))

    def get_states(self):
        return [item.state for item in self]

    def get_actions(self):
        return [item.action for item in self]

    def get_rewards(self):
        return [item.step_reward for item in self]

    def discounted_rewards(self, gamma):
        rewards = np.array([item.step_reward for item in self])
        discounted_r = np.zeros_like(rewards)
        running_add = 0

        for t in reversed(range(rewards.size)):
            running_add = running_add * gamma + rewards[t]
            discounted_r[t] = running_add

        return discounted_r
