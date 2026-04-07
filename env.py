import random

class SmartTrafficEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        # Initial state
        self.cars_left = random.randint(5, 15)
        self.cars_right = random.randint(5, 15)
        self.ambulance = random.choice([0, 1])  # 1 = present

        return self.state()

    def state(self):
        return {
            "cars_left": self.cars_left,
            "cars_right": self.cars_right,
            "ambulance": self.ambulance
        }

    def step(self, action):
        """
        Actions:
        0 = Green Left
        1 = Green Right
        2 = Priority Ambulance
        """

        reward = 0

        # 🚑 Ambulance logic
        if self.ambulance == 1:
            if action == 2:
                reward += 100  # best action
                self.ambulance = 0
            else:
                reward -= 50  # bad decision

        # 🚗 Traffic movement
        if action == 0:
            self.cars_left = max(0, self.cars_left - random.randint(2, 5))
        elif action == 1:
            self.cars_right = max(0, self.cars_right - random.randint(2, 5))

        # New cars arrive
        self.cars_left += random.randint(0, 3)
        self.cars_right += random.randint(0, 3)

        # Reward for reducing traffic
        reward -= (self.cars_left + self.cars_right)

        # Episode never ends (for now)
        done = False

        return self.state(), reward, done, {}