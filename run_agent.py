from inference import reset, step, act

state = reset()
print("Initial State:", state)

for i in range(10):
    action = act(state)
    state, reward, done, _ = step(action)

    print(f"Step {i+1}")
    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)
    print("------")
