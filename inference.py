from env import SmartTrafficEnv
from agent import SmartAgent

env = SmartTrafficEnv()
agent = SmartAgent()

# Reset environment
def reset():
    try:
        state = env.reset()
        return {
            "state": state
        }
    except Exception as e:
        return {
            "error": str(e)
        }

# Step function
def step(action):
    try:
        state, reward, done, info = env.step(int(action))
        return {
            "state": state,
            "reward": reward,
            "done": done,
            "info": info
        }
    except Exception as e:
        return {
            "error": str(e)
        }

# Agent action
def act(state):
    try:
        action = agent.choose_action(state)
        return {
            "action": action
        }
    except Exception as e:
        return {
            "error": str(e)
        }
