class SmartAgent:
    def choose_action(self, state):
        cars_left = state["cars_left"]
        cars_right = state["cars_right"]
        ambulance = state["ambulance"]

        if ambulance == 1:
            return 2

        if cars_left > cars_right:
            return 0
        else:
            return 1