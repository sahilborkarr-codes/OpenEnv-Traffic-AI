from env import SmartTrafficEnv
from agent import SmartAgent
import random

def run_random(env, steps=20):
    state = env.reset()
    total_reward = 0

    for _ in range(steps):
        action = random.choice([0, 1, 2])
        state, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward


def run_smart(env, steps=20):
    agent = SmartAgent()
    state = env.reset()
    total_reward = 0

    for _ in range(steps):
        action = agent.choose_action(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward


env = SmartTrafficEnv()

random_score = run_random(env)
smart_score = run_smart(env)

print("Random Agent Score:", random_score)
print("Smart Agent Score:", smart_score)

if smart_score > random_score:
    print("✅ Smart Agent is better!")
else:
    print("⚠️ Needs improvement")