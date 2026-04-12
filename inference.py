import asyncio
import os
from openai import OpenAI

from env import SmartTrafficEnv
from agent import SmartAgent

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

env = SmartTrafficEnv()
agent = SmartAgent()

def log_start():
    print(f"[START] task=traffic env=openenv model={MODEL_NAME}", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)


def get_action_from_llm(state):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Control traffic efficiently."},
                {"role": "user", "content": str(state)}
            ],
            max_tokens=10
        )
        text = response.choices[0].message.content.strip()

        # simple parsing
        return 0 if "left" in text.lower() else 1
    except:
        return 0


async def main():
    rewards = []
    steps = 0

    log_start()

    state = env.reset()

    for step in range(1, 11):
        action = get_action_from_llm(state)

        state, reward, done, _ = env.step(action)

        rewards.append(reward)
        steps = step

        log_step(step, action, reward, done)

        if done:
            break

    score = max(0, min(1, sum(rewards) / 100))
    success = score > 0.1

    log_end(success, steps, score, rewards)


if __name__ == "__main__":
    asyncio.run(main())