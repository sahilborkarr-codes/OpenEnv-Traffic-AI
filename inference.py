from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

state = {"cars_left": 5, "cars_right": 5, "ambulance": 0}

class Action(BaseModel):
    action: int = 0

@app.get("/")
def home():
    return {"status": "ok"}

# RESET
@app.post("/reset")
def reset():
    global state
    state = {"cars_left": 5, "cars_right": 5, "ambulance": 0}
    return {"observation": state}

# STEP
@app.post("/step")
def step(data: Action):
    global state

    if data.action == 0:
        state["cars_left"] = max(0, state["cars_left"] - 1)
    else:
        state["cars_right"] = max(0, state["cars_right"] - 1)

    reward = -(state["cars_left"] + state["cars_right"])

    return {
        "observation": state,
        "reward": reward,
        "done": False,
        "info": {}
    }

# ACT
@app.post("/act")
def act():
    if state["cars_left"] > state["cars_right"]:
        action = 0
    else:
        action = 1
    return {"action": action}