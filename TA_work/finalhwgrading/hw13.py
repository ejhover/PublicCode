import turtle, random, math

class Game:
    '''
Purpose: Set up the turtle screen size, call the player class and start the game, draw the moon surface, and allow player input 
of arrow keys. 
Instance variables: 
    - player: create the spaceship that the player will control 
Methods: 
    - __init__(self) : Set up the turtle screen size, call the player class and start the game, draw the moon surface, and allow 
    player input of arrow keys. 
    '''
    def __init__(self):
        #Bottom left corner of screen is (0, 0)
        #Top right corner is (500, 500)
        turtle.setworldcoordinates(0, 0, 500, 500)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        #Draw the moon’s surface at the bottom of the screen.
        moon = turtle.Turtle()
        moon.speed(0)
        moon.penup()
        moon.setposition(-7, 20)
        moon.pendown()
        moon.goto(507, 20)
        moon.hideturtle()
        
        #Ensure turtle is running as fast as possible
        turtle.delay(0)
        self.player = SpaceCraft(random.uniform(100, 400), random.uniform(250, 400), random.uniform(-4.0, 4.0), random.uniform(-2.0 , 0))
        self.player.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.turn_left, 'Left')
        turtle.onkeypress(self.player.turn_right, 'Right')
        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

class SpaceCraft(turtle.Turtle):
    '''
Purpose: Allow the spaceship that the player to be playable, update position, create win condition,
call Meteors class, and allow thrust, left and right turn.
Instance variables: 
    - x_vel: the current velocity of the spaceship in the x direction
    - y_vel: the current velocity of the spaceship in the y direction
    - fuel: the amount of fuel left in the spaceship
    - meteors: a list of 8 Meteors objects that the player needs to avoid or land on
    - crashed: a boolean value that is True when the spaceship has crashed and False otherwise
Methods: 
    - __init__(self, x_pos, y_pos, x_vel, y_vel): Initializes the SpaceCraft object with x and y positions, x and y velocities,
    fuel, and meteors. It also sets up the turtle graphics and listens for player inputs.

    - move(self): Updates the position of the SpaceCraft based on its velocity and gravity.

    - gameloop(self): Updates the game state by calling move and checking for collisions with meteors 

    or successful landings.
    - thrust(self): Called when the player inputs the up arrow key. This method adds forward velocity 
    to the SpaceCraft and subtracts fuel.

    - turn_left(self): Called when the player inputs the left arrow key. This method turns the SpaceCraft 
    15 degrees to the left if it has fuel and has not crashed.

    - turn_right(self): Called when the player inputs the right arrow key. This method turns the SpaceCraft
    15 degrees to the right if it has fuel and has not crashed.
    '''    
    # set everything up, fuel, set position of spaceship, and add 8 meteors
    def __init__ (self, x_pos, y_pos, x_vel, y_vel):
        turtle.Turtle.__init__(self)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.fuel = 40
        self.left(90)
        self.penup()
        self.speed(0)
        self.goto(x_pos, y_pos)
        self.crashed = False
        self.meteors = []
        # making 8 meteors
        for i in range (8):
            meteor = Meteors()
            meteor.gameloop()
            self.meteors.append(meteor)
    # update the position of the spaceship of player input and apply physic to the spaceship
    def move(self):
        self.y_vel -= 0.0486
        self.x_pos = self.xcor() + self.x_vel 
        self.y_pos = self.ycor() + self.y_vel 
        self.goto(self.x_pos,self.y_pos)
    # loop the move() so the movement will keep updating until player land, crash landing, or crash into a meteor
    def gameloop(self): 
        self.move()
        for meteor in self.meteors:
            if meteor.M_x_pos - 7 <= self.xcor() <= meteor.M_x_pos + 7 and meteor.M_y_pos - 7 <= self.ycor() <= meteor.M_y_pos + 7:
                print('You crashed!')
                for meteor in self.meteors:
                    meteor.allow_move = False
                self.crashed = True
        if not self.crashed:
            if self.ycor() <= 20: 
                if -3 <= self.x_vel <= 3 and -3 <= self.y_vel <= 3:
                    print("Successful landing!")
                    for meteor in self.meteors:
                        meteor.allow_move = False
                else: 
                    print('You crashed!')
                    for meteor in self.meteors:
                        meteor.allow_move = False
            else: 
                turtle.ontimer(self.gameloop, 30)
    # called when the player input up arrow key. This add forward velocity to the ship
    def thrust(self):
            if self.fuel > 0:
                self.fuel -= 1
                angle_ship = math.radians(self.heading())
                self.x_vel += math.cos(angle_ship)
                self.y_vel += math.sin(angle_ship)
                print(self.fuel)
    #Right now, the player can continue to turn the spacecraft even after the game is over.  Find a way to prevent this from occurring.
    # called when the player input left arrow key. This turn the ship 15 degree to the left
    def turn_left(self):
        if not self.crashed:
            if self.fuel > 0:
                self.fuel -= 1
                angle_ship = math.radians(self.heading()) 
                self.left(angle_ship + 15)
                print(self.fuel)
        else: 
            print("Can't turn now!")
    #Right now, the player can continue to turn the spacecraft even after the game is over.  Find a way to prevent this from occurring.
    # called when the player input right arrow key. This turn the ship 15 degree to the right
    def turn_right(self):
        if not self.crashed:
            if self.fuel > 0:
                self.fuel -= 1
                angle_ship = math.radians(self.heading()) 
                self.left(angle_ship - 15)   
                print(self.fuel)     
        else: 
            print("Can't turn now!")

class Meteors(turtle.Turtle):
    '''
Purpose: The purpose of this class is to create Meteors objects in the game with random initial
position, velocity and appearance, and to handle their movement and position updates during the 
game. It also includes a method to teleport the meteors back to the screen when they go off-screen,
so that there are always 8 meteors visible on the screen.
Instance variables: 
    - M_x_pos: a float representing the x-position of the meteor.
    - M_y_pos: a float representing the y-position of the meteor.
    - M_x_vel: a float representing the x-velocity of the meteor.
    - M_y_vel: a float representing the y-velocity of the meteor.
    - allow_move: a boolean representing whether the meteor is allowed to move or not.
Methods: 
    - __init__(self): This method initializes a new instance of the class with random starting position
    and velocity. It sets up the instance variables M_x_pos, M_y_pos, M_x_vel, and M_y_vel to random 
    values, and uses the turtle module to set up the turtle graphics and hide the turtle.

    - move(self): This method updates the position of the meteor by adding its x and y velocity to its 
    current position. It also uses the turtle module to clear the previous position of the meteor and 
    redraw it in its new position.

    - gameloop(self): This method is the main loop of the game. It calls the move() method to update the 
    position of the meteor, and checks if the meteor has gone off the screen. If it has, it randomly teleports 
    the meteor to a new position in the middle of the screen and gives it a new random velocity. The method then 
    uses the turtle module to schedule itself to be called again after a short delay, creating a loop that 
    continuously updates the position of the meteor.
    '''
    # set up everything that will allow the Meteors to render and move at randoms with random velocity
    def __init__ (self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.M_x_pos = random.uniform(100, 400)
        self.M_y_pos = random.uniform(100, 400)
        self.M_x_vel = random.uniform(-4.0, 4.0)
        self.M_y_vel = random.uniform(-2.0 , 0)
        self.setposition(self.M_x_pos, self.M_y_pos)
        self.dot(15, 'blue')
        self.hideturtle()
        self.allow_move = True
    # update the movement of the Meteors
    def move(self):
        self.clear()
        self.M_x_pos = self.xcor() + self.M_x_vel 
        self.M_y_pos = self.ycor() + self.M_y_vel 
        self.goto(self.M_x_pos, self.M_y_pos)        
        self.dot(15, 'blue')
    # loop the move() and teleport any Meteors that go off screen randomly in the middle to always have 8 Meteors on screen
    def gameloop(self): 
        if self.allow_move:
            self.move()
            if self.ycor() <= 0 or self.ycor() >= 507 or self.xcor() <= -7 or self.xcor() >= 500:
                self.setposition(random.uniform(100, 400),random.uniform(100, 400)) 
                self.M_x_vel = random.uniform(-4.0, 4.0)
                self.M_y_vel = random.uniform(-2.0 , 0) 
            turtle.ontimer(self.gameloop, 30)


# if __name__ == '__main__':
#     Game()

#Draw the moon’s surface at the bottom of the screen. 
#Right now, the player can continue to turn the spacecraft even after the game is over.  Find a way to prevent this from occurring.