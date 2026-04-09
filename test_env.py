from env import SmartTrafficEnv
import random

env = SmartTrafficEnv()

state = env.reset()
print("Initial State:", state)

for i in range(10):
    action = random.choice([0, 1, 2])
    state, reward, done, _ = env.step(action)

    print(f"Step {i+1}")
    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)
    print("------")
