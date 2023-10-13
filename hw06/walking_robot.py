# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Homework 6
'''import Robot and Board classes from robot.py and board.py to use them with the walking robot'''
from robot import Robot
from board import Board
class WalkingRobot(Robot):
    '''initialize walking robot class and inherit Robot class'''
    def __init__(self, model_name="", environment=Board(), current_location=(0, 0)):
        '''initialize the inherited traits of the Robot'''
        super().__init__(model_name, environment, current_location)
    def step(self, direction):
        '''move the current location and update the board with new robot location given direction'''
        # dictionary holding the offsets of the different directions
        dire = {"N": (-1,0), "S": (1,0), "E": (0,1), "W": (0,-1)}
        self.current_location = (dire[direction][0] + self.current_location[0],
                                dire[direction][1] + self.current_location[1])
        self.environment.update(self.current_location)
    def move(self, destination):
        '''move the robot to a give destination step by step using above step function'''
        vert_steps = destination[0] - self.current_location[0]
        horiz_steps = destination[1] - self.current_location[1]
        # dict tracks if a string is in the positive direction(0) or the negative direction(1)
        direction_dict = {0: ("S", "E"), 1: ("N", "W")}
        vert_direction = 0 if vert_steps >= 0 else 1
        horiz_direction = 0 if horiz_steps >= 0 else 1
        for _ in range(abs(vert_steps)):
            self.step(direction_dict[vert_direction][0])
        for _ in range(abs(horiz_steps)):
            self.step(direction_dict[horiz_direction][1])
