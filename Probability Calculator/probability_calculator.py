#This is my solution to the Probability Calculator Problem in FCC's Scientific Computing with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-probability-calculator-solution

import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
      #uses **kwargs due to the class itself taking multiple keyword arguments
        self.kwargs = kwargs
        self.contents = []
        for keys, values in self.kwargs.items():
            for values in range(0, values):
                self.contents.append(keys)

    def draw(self, to_remove_balls):

        removed_balls = []

        if int(to_remove_balls) > len(self.contents):
            return self.contents
        else:
            for i in range(0, to_remove_balls):
              #this removes a random ball on initial list based on index. Because it removes using index, error will occur if the random value is equal to the len value. The index of self.contents shift and the last index is always less 1 of the len of the list.
                remove = self.contents.pop(random.randint(0, len(self.contents)-1))
                removed_balls.append(remove)
            return removed_balls

            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #this counts the times where we meet the conditions in expected balls
    ball_found_count = 0

    
    for i in range(0, num_experiments):
        hats = copy.deepcopy(hat)
        draw_balls = hats.draw(num_balls_drawn)
        #this counts the balls that meet the initial criteria for their values
        ball_found = 0
        for keys, values in expected_balls.items():
            if draw_balls.count(keys) >= values :
                ball_found +=1
        #this checks if all balls in expected balls meet their criteria in the draw
        if ball_found == len(expected_balls):
            ball_found_count += 1

    probability = float(ball_found_count/num_experiments)

    return probability
    