from flask import Flask, request, jsonify

app = Flask(__name__)

state = {}

# RESET (VERY IMPORTANT FORMAT)
@app.route("/reset", methods=["POST"])
def reset():
    global state
    state = {
        "cars_left": 5,
        "cars_right": 5,
        "ambulance": 0
    }

    return jsonify({
        "observation": state
    })


# STEP (VERY IMPORTANT FORMAT)
@app.route("/step", methods=["POST"])
def step():
    global state

    data = request.get_json(force=True)
    action = data.get("action", 0)

    if action == 0:
        state["cars_left"] = max(0, state["cars_left"] - 1)
    else:
        state["cars_right"] = max(0, state["cars_right"] - 1)

    reward = -(state["cars_left"] + state["cars_right"])

    return jsonify({
        "observation": state,
        "reward": reward,
        "done": False,
        "info": {}
    })


# ACT
@app.route("/act", methods=["POST"])
def act():
    data = request.get_json(force=True)
    s = data.get("state", state)

    action = 0 if s["cars_left"] > s["cars_right"] else 1

    return jsonify({
        "action": action
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)