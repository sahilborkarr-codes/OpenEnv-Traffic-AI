import streamlit as st
from env import SmartTrafficEnv
from agent import SmartAgent

st.title("🚦 Smart Traffic AI Simulator")

env = SmartTrafficEnv()
agent = SmartAgent()

state = env.reset()

st.write("### Initial State")
st.write(state)

for i in range(5):
    action = agent.choose_action(state)
    state, reward, done, _ = env.step(action)

    st.write(f"### Step {i+1}")
    st.write("Action:", action)
    st.write("State:", state)
    st.write("Reward:", reward)