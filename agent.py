class SmartAgent:
    def choose_action(self, state):
        cars_left, cars_right, ambulance = state

        if ambulance == 1:
            return 2

        if cars_left > cars_right:
            return 0
        else:
            return 1
