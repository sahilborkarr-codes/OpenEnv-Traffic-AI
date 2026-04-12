import asyncio
import os

from my_env_v4 import MyEnvV4Env, MyEnvV4Action

async def main():
    # IMPORTANT: use local docker image
    IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

    env = await MyEnvV4Env.from_docker_image(IMAGE_NAME)

    print("[START] task=test env=openenv model=baseline", flush=True)

    result = await env.reset()

    rewards = []
    steps = 0

    for step in range(1, 6):
        if result.done:
            break

        action = MyEnvV4Action(message="hello world")

        result = await env.step(action)

        reward = result.reward or 0.0
        done = result.done

        rewards.append(reward)
        steps = step

        print(f"[STEP] step={step} action=hello reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

    score = min(1.0, sum(rewards) / 10)

    print(f"[END] success=true steps={steps} score={score:.2f} rewards={','.join(f'{r:.2f}' for r in rewards)}", flush=True)

    await env.close()

if __name__ == "__main__":
    asyncio.run(main())