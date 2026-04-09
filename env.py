import random

class SmartTrafficEnv:
    def __init__(self):
        self.cars_left = 0
        self.cars_right = 0
        self.ambulance = 0

    
    def reset(self):
        self.cars_left = random.randint(5, 15)
        self.cars_right = random.randint(5, 15)
        self.ambulance = random.choice([0, 1])

       
        return [self.cars_left, self.cars_right, self.ambulance]

    def step(self, action):
        reward = 0

        
        if self.ambulance == 1:
            if action == 2:
                reward += 100
                self.ambulance = 0
            else:
                reward -= 50

        
        if action == 0:
            self.cars_left = max(0, self.cars_left - random.randint(2, 5))
        elif action == 1:
            self.cars_right = max(0, self.cars_right - random.randint(2, 5))

        
        self.cars_left += random.randint(0, 3)
        self.cars_right += random.randint(0, 3)

        reward -= (self.cars_left + self.cars_right)

        next_state = [self.cars_left, self.cars_right, self.ambulance]

        done = False
        info = {}

        return next_state, reward, done, info
