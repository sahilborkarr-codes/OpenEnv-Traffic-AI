# 🚦 OpenEnv – Smart Traffic AI Simulator

## 📌 Problem

Urban areas face traffic congestion and delayed emergency response. There is no intelligent system that dynamically optimizes traffic in real time.

## 💡 Solution

We built an OpenEnv-based simulation where an AI agent learns to manage traffic and prioritize emergency vehicles using a step-based environment.

## ⚙️ Environment API

* `reset()` → initializes environment
* `step(action)` → returns (state, reward, done, info)
* `state()` → current state

## 🤖 Agent

A rule-based intelligent agent that:

* Prioritizes ambulance movement 🚑
* Optimizes traffic flow 🚦

## 📊 Results

Smart Agent vs Random Agent:

* Random Score: -496
* Smart Score: -117
  👉 Significant improvement observed


## 🛠️ Tech Stack

* Python
* Gradio
* OpenEnv concepts

## 🚀 Future Scope

* Multi-signal system
* Real-time traffic data integration
* Reinforcement learning model
