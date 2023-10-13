import turtle
import random
#To play the game you can use the W and S keys to move your paddle up and down to bounce and ball back and hopefully knock it behind the other paddle
#initializing score and paddle direction variables
score = 0
go = 0
#creating the lists that store high scores
leaderboard_names = ["Emmet"]
leaderboard_scores = [1]
playername = "Emmet"
#initializing background colors, the size of the screen, and the left and right paddles 
turtle.bgcolor("gold")
wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
moving_line = turtle.Turtle()
moving_line.penup()
moving_line.speed(0)
moving_line.goto(-350, 0)
moving_line2 = turtle.Turtle()
moving_line2.penup()
moving_line2.speed(0)
moving_line2.goto(350, 0)
#creating rectangle shape of the paddles and assigning it to their turtles
rectcors = ((10, -70),(10,70),(-10,70),(-10,-70))
wn.register_shape("rectangle", rectcors)
moving_line.shape("rectangle")
moving_line2.shape("rectangle")
#creating ball bouncing around screen
bball = turtle.Turtle()
bball.shape("circle")
bball.goto(0, 0)
bball.penup()
bball.setheading(random.randint(-45, 45))
#creating the turtle used to write the score and shrinking the turtle so it can't be seen 
score_drawer = turtle.Turtle()
score_drawer.speed(0)
score_drawer.penup()
score_drawer.shapesize(0.00000000001)
moving_line.speed(1)
moving_line2.speed(1)
moving_line.setheading(90)
moving_line2.setheading(90)
#functions for the top and bottom walls and for the paddles to calculate the reference angle which the ball should head after touching the object
def paddle_ref_angle(ang):
    return(180-ang)
def wall_ref_angle(ang):
    return(-1*ang)
#making function which changes the direction of the paddles when they leave the screen vertically
def line_direction():
    if go == 0: 
        moving_line.fd(10)
    if go == 1: 
        moving_line.bk(10)
#asks user for desired gamemode and changes the speed of the paddles and the ball based on the difficulty
gamemode = 0
#int(input("Which Gamemode? (Easy: 0, Normal: 1, or Hard: 2)"))
#I make the speeds of the ball and paddles their own variables so I can use them throughout the program based on what they were assigned with the game mode
if gamemode == 0:
    spe = 2 
    moving_line.speed(spe) 
    ballspe = 1 
    bball.speed(ballspe)
if gamemode == 1:
    spe = 3 
    moving_line.speed(spe) 
    ballspe = 2 
    bball.speed(ballspe)
if gamemode == 2:
    spe = 4 
    moving_line.speed(spe) 
    ballspe = 3 
    bball.speed(ballspe)
#functions I use to move the paddles for both 1 and two player by changing the y coordinate and later utilize these functions onkeypress
def up():
    moving_line2.speed(0)
    y = moving_line2.ycor()
    y += 40 
    moving_line2.sety(y) 
    moving_line2.speed(spe)
def down(): 
    moving_line2.speed(0) 
    y = moving_line2.ycor()
    y -= 40 
    moving_line2.sety(y) 
    moving_line2.speed(spe)
ant = 0
#start the program to be able to run the functions that mode the paddles up and down when you press the corresponding "Up" and "Down" arrows
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
#setting leaderboard drawing turtle to go to the top of the screen and write the top scoring person on the leaderboard and the score-drawing turtle to write the inital score along with the 
old_score_drawer = turtle.Turtle()
old_score_drawer.penup()
old_score_drawer.hideturtle()
old_score_drawer.goto(0, 250)
score_drawer.goto(-140, 200)
score_drawer.write("Your score is " + str(score), font=("Arial", 40, "normal")) 
old_score_drawer.write("High Score: " + leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))] + " - " + str(max(leaderboard_scores)), align="center", font=("Arial", 20, "normal"))
#leaderboard function which checks if their score is the new high score and if it's not it displays a message. If it is, it replaces their name with their score on top and if they don't want to play again, it writes the high score holder's name on the screen
def leaderboard_check(score, ans):
    if score > max(leaderboard_scores):
        old_score_drawer.clear()
        playername = input("You got the high score! What's your name? ") 
        leaderboard_scores.append(score) 
        leaderboard_names.append(playername) 
        old_score_drawer.write("High Score: " + leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))] + " - " + str(max(leaderboard_scores)), align="center", font=("Arial", 20, "normal"))
    else:
        print("Ahh!! Not quite good enough to beat " + leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))]) 
        x = -1*(560/len(leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))]))*(len(leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))])/2)
    if ans == "n":
        bball.clear()
        for i in leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))]:
            old_score_drawer.goto(x, random.randint(-200, 200))
            old_score_drawer.write(i, align="center", font=("Arial", 70, "normal"))
            x += 560/len(leaderboard_names[leaderboard_scores.index(max(leaderboard_scores))])

 #initializing variable which keeps the loop going to be able to break out of the loop by adding to the variable
while True:
    #update the screen, and move the turtle forward 10 pixels at the start of every loop wn.update()
    bball.fd(10)
    #running function to change the direction of the automatically running paddle until it hits the other side of the screen
    line_direction()
    #detecting if the ball touches the top or bottom of the screen and setting its heading to its reference angle and moving it away in that direction
    if abs((int(bball.ycor())) > 285) or (int(bball.ycor()) < -285):
        bball.speed(0) 
        bball.setheading(wall_ref_angle(bball.heading())) 
        bball.speed(ballspe)
        bball.fd(20)
    #detects if the person scores a point and adds to their score, updates the score-drawing turtle, and resets the ball to start in the middle again
    if (int(bball.xcor()) < -380):
        score_drawer.clear()
        score += 1
        score_drawer.write("Your score is " + str(score), font=("Arial", 40, "normal")) 
        bball.speed(0)
        bball.goto(0, 0) 
        bball.setheading(random.randint(-45, 45)) 
        bball.speed(ballspe)
    #detecs if the ball hits either paddle and sets its heading to its reference angle and moves it forward
    if (abs(bball.xcor() - moving_line.xcor()) < 25 and abs(bball.ycor() - moving_line.ycor()) < 110) or (abs(bball.xcor() - moving_line2.xcor()) < 25 and abs(bball.ycor() - moving_line2.ycor()) < 110):
        bball.speed(0) 
        bball.setheading(paddle_ref_angle(bball.heading())) 
        bball.speed(ballspe)
        bball.fd(20)
    #checks if auto-paddle hits either side of the screen and adds to the variable which changes the line_direction() function to change its direction
    if moving_line.ycor() == 280: 
        go += 1
    if moving_line.ycor() == -280: 
        go -= 1
    #detects if the ball goes behind their own paddle and gets scored on. If so, resets the whole screen and displays Game Over message and prompts if they want to play again which decides whether or not it runs through the loop again
    if (int(bball.xcor()) > 380):
        bball.hideturtle()
        score_drawer.clear()
        bball.speed(0)
        bball.goto(0, 0)
        bball.write("Game Over, Your Score Was " + str(score), align="center", font=("Arial", 40, "normal"))
        moving_line2.goto(350, 0)
        moving_line.goto(-350, 0)
        #asks if they want to play again and if they do then it continues thorugh the loop and sets up the score drawer again
        ans = input("Would you like to play again?(y/n)") 
        if ans == "y":
            #checks if the person's score is the new high score and if it is it adds them to the list and displays their high score
            leaderboard_check(score, "y")
            #reset the board and the score to start a new game
            score = 0
            score_drawer.goto(-140, 200)
            score_drawer.write("Your score is " + str(score), font=("Arial", 40, "normal")) 
            bball.clear()
            bball.speed(1)
            bball.goto(0, 0)
            bball.setheading(random.randint(-45, 45))
            bball.speed(ballspe)
            bball.showturtle()
            continue
        if ans == "n":
            leaderboard_check(score, "n")
    #when they don't want to play again this ends the loop break
    wn.mainloop()

