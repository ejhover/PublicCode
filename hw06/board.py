# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Homework 6
class Board:
    '''initializes the Board class to hold position of the robot and the size of the board'''
    def __init__(self, height=10, width=10, robot_location=(0, 0)):
        '''initializes board dimensions and the location of the robot'''
        self.height = height
        self.width = width
        self.robot_location = robot_location # (row, column); (y, x)
        # uses generator object to construct board matrix with robot location
        self.board_space = [["-" if (j, i) != (self.robot_location) else "R"
                            for i in range(self.width)] for j in range(self.height)]
    def __repr__(self):
        '''prints out the board matrix in string format'''
        return "\n".join([" ".join(i) for i in self.board_space])
    def update(self, new_location):
        '''changes the robot's location and updates the board with its location'''
        self.board_space[self.robot_location[0]][self.robot_location[1]] = "-"
        self.board_space[new_location[0]][new_location[1]] = "R"
        self.robot_location = new_location
    def get_location(self):
        '''returns the current location of the robot on the board'''
        return self.robot_location
