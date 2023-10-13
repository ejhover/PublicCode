# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Homework 6
'''import board class from board.py to utilize Board class'''
from board import Board
class Robot:
    '''initilize Robot class which is held on the board'''
    def __init__(self, model_name="", environment=Board(), current_location=(0, 0)):
        '''initialize the model_name, board environment, and the robot's location'''
        self.model_name = model_name
        self.current_location = current_location
        self.environment = environment
        self.environment.update(self.current_location)
    def move(self, destination):
        '''move the robot to a given location on the board and update the board'''
        self.current_location = destination
        self.environment.update(destination)
    def __repr__(self):
        '''returns the board matrix in string format'''
        return self.environment.__repr__()
