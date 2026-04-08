from env import SmartTrafficEnv
from agent import SmartAgent

env = SmartTrafficEnv()
agent = SmartAgent()

def reset():
    try:
        state = env.reset()
        return {"state": state}
    except Exception as e:
        return {"error": str(e)}

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
        return {"error": str(e)}

def act(state):
    try:
        action = agent.choose_action(state)
        return {"action": action}
    except Exception as e:
        return {"error": str(e)}