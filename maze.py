#imports needed libraries
import turtle
import random


#Defines unit class. 
#This class contain the information for each square on the maze
class unit():
  #assigns a blank square when initialised
  def __init__(self):
    #self.txt is an array of walls and paths
    self.txt = [[0,0,0],[0,1,0],[0,0,0]]
  
  #changes the value of the maze based on a direction given
  def changeVal(self,direction):
    #if the program is given the direction 'up'
    #it changes the top value in the units txt
    #self.txt contains the information on where walls are
    if direction == 'up':
      self.txt[0][1] = 1 
    elif direction == 'dw':
      self.txt[2][1] = 1 
    elif direction == 'lf':
      self.txt[1][0] = 1 
    elif direction == 'rt':
      self.txt[1][2] = 1 

#Defines the checker class
class checker():
  def __init__(self,x,y,dr):
    self.x = x      #X pos
    self.y = y      #Y pos
    self.dr = dr    #direction
    self.xFar = 0   #Farthest X "traveled"
    self.yFar = 0   #Farthest Y "traveled"
    self.d = 0      #Current distance "traveled"
    self.dFar = 0   #Farthest distance "traveled"
    self.drs = ['rt','up','lf','dw'] #All possible direction
  
  #Return the new Y pos based on current direction
  def next_y(self):
    if self.dr == 'up':
      return self.y - 1 if self.y != 0 else none
    elif self.dr == 'dw':
      return self.y + 1
    else:
      return self.y
    
  #Return the new X pos based on current direction  
  def next_x(self):
    if self.dr == 'lf':
      return self.x - 1 if self.x != 0 else none
    elif self.dr == 'rt':
      return self.x + 1
    else:
      return self.x
  
  #Returns the opposite of the direction facing
  def drNot(self):
    if self.dr == 'up':     #up becomes down
      return 'dw'
    elif self.dr == 'dw':   #down becomes up
      return 'up'
    elif self.dr == 'lf':   #left becomes right
      return 'rt'
    elif self.dr == 'rt':   #right becomes left
      return 'lf'
  
  #moves the checker forward to the next location based on direction
  def move(self):
    self.x = self.next_x()
    self.y = self.next_y()
    
  #moves the checker backwards
  def moveBack(self):
      self.dr = self.drNot()
      self.move()
      self.dr = self.drNot()
  
  #Rotates the checker 90 degrees clockwise
  def rotate(self):
    self.dr = self.drs[(self.drs.index(self.dr)+1)%4]
  
  
  #Sets the checkers direction a random direction
  def random(self):
    if random.random() < 0.5:
      self.dr = random.choice([i for i in self.drs if i != self.dr])
  
  #If the current distance is greater than the max distance
  #it sets the max distance to the current distance
  def record(self):
    if self.dFar < self.d:
      self.dFar = self.d
      self.yFar = self.y
      self.xFar = self.x

#Defines maze class
class maze():
  
  #Creates a new maze
  def reset(self,x,y):
    #creates a empty maze x units long and y units tall
    self.mz = [[unit() for i in range(x)] for j in range(y)]
    self.x = x #stores the length of the maze
    self.y = y #stores the height of the maze
    #determines the maximum window size to print the maze on
    self.space = 400/max(2*self.x,2*self.y)
  
  #Changes thw walls in front of the checker
  def change(self, check):
    self.mz[check.y][check.x].changeVal(check.dr)
    self.mz[check.next_y()][check.next_x()].changeVal(check.drNot())
  
  #the next two funtions are what actually creates the maze
  
  def draw(self, check):
    self.change(check) #This starts out by creating a path in the maze
    check.move() #then it checker "moves" to the next square
    check.d = check.d + 1 #increates distance traveled by 1
    check.record() #checks if this is the current farthest point
    self.drTry(check, check.dr) #trys the edges around it
    #drTry() has the function draw() in it, do it is able to repeate
    check.moveBack() #moves back
    check.d = check.d - 1 #decreases the distance by 1
  
  #tries to  
  def drTry(self, check, dr):
    check.random() #sets the checkers direction to a random direction
    for i in range(4): #loops three times
      try: #this allows the program to continue if the next sqaure tested would be outside of its range
        if self.mz[check.next_y()][check.next_x()].txt == [[0,0,0],[0,1,0],[0,0,0]]:
          #^ checks if the next square is blank
          #if so, it moves to it and repeates
          self.draw(check)
      except: #needed for try statment
        pass  #needed for try statment
      check.rotate() #rotates the checker 90 degrees
    check.dr = dr #resets direction 

    
  #Formats the maze into a version that can be printed
  def formatMaze(self,check,robot):
    robot.ext = (2*check.xFar,2*check.yFar) #sets the exit of the maze
    newMaze=[]
    for row in self.mz:
      #cuts out all of the extra parts of the maze
      for i in [1,2]:
        newMaze.append([row[j].txt[i][k] for j in range(len(row)) for k in [1,2]])
    self.fmz = newMaze #sets formated maze

#this is the objet that moves thought the maze
class Robot():
  def __init__(self, Maze): #initializes the maze
    self.x = 0
    self.y = 0
    self.Maze = Maze #assignes the maze to make it easier to axcess
    self.trt = turtle.Turtle() #creates a turtle object
    self.trt.shape("turtle") #modifies the turtle
    self.trt.fillcolor("blue") #modifies the turtle
    self.trt.penup() #modifies the turtle
  
  #resets the turtle
  def start(self):
    self.x = 0
    self.y = 0
    self.trt.speed(0)
    self.trt.goto(-200+Maze.space*0.5,200-Maze.space*0.5)
    #^ goes to the start of the maze
    self.trt.speed(10)
  
  #the next four funtions move the turlte when a key is pressed 
  #wasd movement
  def w(self):
    if self.Maze.fmz[self.y-1][self.x] != 0 and self.y-1 >= 0:
      #^ checks if the next square is the not a wall and inside the maze
      self.y -= 1 #changes pos values
      self.trt.setheading(90) #changes turtle direction
      self.trt.fd(Maze.space) #moves forward
      if (self.x,self.y) == self.ext:
        #^ if the turtle is at the exit
        reset() #the maze is reset
  def a(self):
    if self.Maze.fmz[self.y][self.x-1] != 0 and self.x-1 >= 0:
      self.x -= 1
      self.trt.setheading(180)
      self.trt.fd(Maze.space)
      if (self.x,self.y) == self.ext:
        reset()
  def s(self):
    if self.Maze.fmz[self.y+1][self.x] != 0:
      self.y += 1
      self.trt.setheading(270)
      self.trt.fd(Maze.space)
      if (self.x,self.y) == self.ext:
        reset()
  def d(self):
    if self.Maze.fmz[self.y][self.x+1] != 0:
      self.x += 1
      self.trt.setheading(0)
      self.trt.fd(Maze.space)
      if (self.x,self.y) == self.ext:
        reset()

#draws the maze on the scren
def drawMaze(Maze):
  screen.tracer(0)
  #for each square in the maze
  for y, row in enumerate(Maze.fmz):
    for x, val in enumerate(row):
      #go to the corner of the square
      painter.goto(-200+Maze.space*x,200-Maze.space*y)
      painter.begin_fill()
      #sets the color to black if there is a wall
      #sets the color to grey if ther is a wall
      painter.fillcolor(["black","grey"][val])
      #draws a square
      for i in range(4):
        painter.fd(Maze.space)
        painter.right(90)
      painter.end_fill()
  #draws the exit
  painter.pencolor("red")
  painter.goto(-200+(2*check.xFar+0.5)*Maze.space,200-(2*check.yFar+0.5)*Maze.space)
  painter.dot(Maze.space)
  screen.tracer(1)
  painter.ht

#Builds the maze
Maze = maze() #creates a maze
check = checker(0,0,'rt') #creates a checker
painter = turtle.Turtle() #creates the object that draws the maze
painter.speed(0) #Changes painter settings
painter.penup() #Changes painter settings
painter.ht() #Changes painter settings
screen = turtle.Screen() #Changes painter settings
robot = Robot(Maze) #creates a the turtle that moves in the maze
screen.onkeypress(robot.w,"w")
screen.onkeypress(robot.a,"a")
screen.onkeypress(robot.s,"s")
screen.onkeypress(robot.d,"d")
screen.listen()
size = 10 #size of the maze

def reset():
  global size
  global Maze
  global check
  global robot
  size +=1
  Maze.reset(size,size)
  Maze.draw(check)
  Maze.formatMaze(check,robot)
  drawMaze(Maze)
  robot.start()

reset()
screen.mainloop()
'''
[0,0,0]
[0,1,1]
[0,1,0]
'''




