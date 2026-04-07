from env import SmartTrafficEnv
from agent import SmartAgent

env = SmartTrafficEnv()
agent = SmartAgent()

state = env.reset()
print("Initial State:", state)

for i in range(10):
    action = agent.choose_action(state)
    state, reward, done, _ = env.step(action)

    print(f"Step {i+1}:")
    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)
    print("-----------")