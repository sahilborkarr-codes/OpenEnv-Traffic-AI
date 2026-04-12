import asyncio
from env import SmartTrafficEnv
from agent import SmartAgent

env = SmartTrafficEnv()
agent = SmartAgent()

def log_start():
    print("[START] task=traffic env=openenv model=smart-agent", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)


async def main():
    rewards = []
    steps = 0

    log_start()

    state = env.reset()

    for step in range(1, 11):
        action = agent.choose_action(state)

        state, reward, done, _ = env.step(action)

        rewards.append(reward)
        steps = step

        log_step(step, action, reward, done)

        if done:
            break

    score = max(0, min(1, sum(rewards) / 100))  # normalize
    success = score > 0.1

    log_end(success, steps, score, rewards)


if __name__ == "__main__":
    asyncio.run(main())