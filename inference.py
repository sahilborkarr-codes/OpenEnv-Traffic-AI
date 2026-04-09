from env import SmartTrafficEnv
from agent import SmartAgent

env = SmartTrafficEnv()
agent = SmartAgent()


def reset():
    return env.reset()


def step(action):
    state, reward, done, info = env.step(int(action))
    return state, reward, done, info


def act(state):
    return agent.choose_action(state)
