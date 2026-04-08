from env import SmartTrafficEnv
from agent import SmartAgent

env = SmartTrafficEnv()
agent = SmartAgent()

# Reset environment
def reset():
    state = env.reset()
    return {"state": state}

# Take action
def step(action: int):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

# Agent action
def act(state):
    action = agent.choose_action(state)
    return {"action": action}