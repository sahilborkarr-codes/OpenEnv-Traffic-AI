from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple test state
state_data = {"cars_left": 5, "cars_right": 5, "ambulance": 0}

@app.route("/", methods=["GET"])
def home():
    return "API Running"

# RESET endpoint (VERY IMPORTANT)
@app.route("/reset", methods=["POST"])
def reset():
    global state_data
    state_data = {"cars_left": 5, "cars_right": 5, "ambulance": 0}
    return jsonify({"state": state_data})

# STEP endpoint
@app.route("/step", methods=["POST"])
def step():
    data = request.get_json(force=True)
    action = data.get("action", 0)

    # simple logic
    if action == 0:
        state_data["cars_left"] = max(0, state_data["cars_left"] - 2)
    elif action == 1:
        state_data["cars_right"] = max(0, state_data["cars_right"] - 2)

    reward = -(state_data["cars_left"] + state_data["cars_right"])

    return jsonify({
        "state": state_data,
        "reward": reward,
        "done": False,
        "info": {}
    })

# ACT endpoint
@app.route("/act", methods=["POST"])
def act():
    data = request.get_json(force=True)
    state = data.get("state", state_data)

    # simple decision
    if state["cars_left"] > state["cars_right"]:
        action = 0
    else:
        action = 1

    return jsonify({"action": action})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)