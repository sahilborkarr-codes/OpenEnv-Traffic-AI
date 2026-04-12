from flask import Flask, request, jsonify
from env import SmartTrafficEnv
from agent import SmartAgent

app = Flask(__name__)

env = SmartTrafficEnv()
agent = SmartAgent()

@app.route('/reset', methods=['POST'])
def reset():
    state = env.reset()
    return jsonify({"state": state})

@app.route('/step', methods=['POST'])
def step():
    data = request.get_json()
    action = data.get("action", 0)

    state, reward, done, info = env.step(action)

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    })

@app.route('/act', methods=['POST'])
def act():
    data = request.get_json()
    state = data.get("state")

    action = agent.choose_action(state)
    return jsonify({"action": action})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)