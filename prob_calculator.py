import copy
from collections import Counter
import random

class Hat:
    def __init__(self, **kwargs):
        #print(kwargs,"initial")
        self.contents = []
        for ball in kwargs:
            for i in range(kwargs[ball]):
                self.contents.append(ball)


    def draw(self, number):
        if len(self.contents) <= number:
            return self.contents

        drawn_balls = []
        contents = self.contents

        for i in range(number):
            ball = random.choice(contents)
            drawn_balls.append(ball)
            contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiments = []
    for i in range(num_experiments):
        hat_exp = copy.deepcopy(hat)
        result = hat_exp.draw(num_balls_drawn)
        ##print(result)
        result = dict(Counter(ball for ball in result))
        ##print(result)
        experiments.append(result)
    ##print(experiments)
    failed = []
    for ball in list(expected_balls.keys()):
        for i in experiments:
            if not(ball in list(i.keys())):
                failed.append(i)

    experiments = [i for i in experiments if i not in failed]
    ##print("start",experiments,"hello")

    failed = []
    for ball in list(expected_balls.keys()):
        for i in experiments:
            if int(expected_balls[ball]) > int(i[ball]):
                failed.append(i)

    experiments = [i for i in experiments if i not in failed]  

    return len(experiments) / num_experiments