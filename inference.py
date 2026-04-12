from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({"observation": {"ok": True}})

@app.route("/step", methods=["POST"])
def step():
    return jsonify({
        "observation": {"ok": True},
        "reward": 0,
        "done": False,
        "info": {}
    })

@app.route("/act", methods=["POST"])
def act():
    return jsonify({"action": 0})

@app.route("/", methods=["GET"])
def home():
    return "running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)