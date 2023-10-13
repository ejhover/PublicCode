# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Exam 01 Problem 1
import random
import turtle as trtl
# opens text file of hangman words and returns random one
def pick_random_word(words):
    # create list of the lines in the text file
    word_list = words.readlines()
    for pos, i in enumerate(word_list):
        # avoid cutting off part of the last word
        if pos == len(word_list)-1:
            break
        # take \n off every word to get the raw word
        word_list[pos] = i[:-1]
    words.close()
    # pick random word from list
    return(random.choice(word_list))
# displays starting screen of the empty gallows and underscores using turtles
def display_gallows(turtle, hangman_screen):
    # draws gallows
    turtle.speed(0)
    hangman_screen.setup(500, 500)
    turtle.penup()
    turtle.left(90)
    turtle.fd(110)
    turtle.pendown()
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(150)
    turtle.lt(90)
    turtle.fd(300)
    turtle.rt(90)
    turtle.fd(80)
    turtle.rt(180)
    turtle.fd(160)
    turtle.penup()
# delete displayed letter and have turtle displayed new found letters
def update_gallows(displayed_characters, update_turtle):
    update_turtle.speed(0)
    update_turtle.penup()
    update_turtle.clear()
    update_turtle.goto(0, -150)
    update_turtle.write(f'{" ".join(displayed_characters)}', align="center", font=("Verdana", 30, "normal"))
# add body parts based on how many wrong guesses
def add_body_part(wrong_guesses, body_turtle):
    # 7 wrong guesses
    body_turtle.speed(0)
    body_turtle.penup()
    if wrong_guesses == 1:
        # write head
        body_turtle.goto(0, 50)
        body_turtle.pendown()
        body_turtle.circle(30)
    if wrong_guesses == 2:
        # write body
        body_turtle.goto(0, 50)
        body_turtle.setheading(-90)
        body_turtle.pendown()
        body_turtle.fd(100)
    if wrong_guesses == 3:
        # write right arm
        body_turtle.goto(0, 0)
        body_turtle.setheading(45)
        body_turtle.pendown()
        body_turtle.fd(30)
    if wrong_guesses == 4:
        # write left arm
        body_turtle.goto(0, 0)
        body_turtle.setheading(135)
        body_turtle.pendown()
        body_turtle.fd(30)
    if wrong_guesses == 5:
        # write right leg
        body_turtle.goto(0, -50)
        body_turtle.setheading(-75)
        body_turtle.pendown()
        body_turtle.fd(40)
    if wrong_guesses == 6:
        # write left leg
        body_turtle.goto(0, -50)
        body_turtle.setheading(255)
        body_turtle.pendown()
        body_turtle.fd(40)
    if wrong_guesses == 7:
        # clear the body when out of guesses
        body_turtle.clear()
# display win screen
def win_sequence(turtle, update_turtle, body_turtle):
    # clear all turtles and write you won
    print("You got it right!")
    turtle.goto(0, 0)
    turtle.clear()
    update_turtle.clear()
    body_turtle.clear()
    turtle.write("You won!", align="center", font=("Verdana", 50, "normal"))
    print("Good game")
# display lose screen
def lose_sequence(turtle, update_turtle, body_turtle, answer):
    # clear all turtles and write game over
    print(f'You failed! The word was {answer}')
    body_turtle.clear()
    update_turtle.clear()
    turtle.clear()
    turtle.goto(0, 0)
    turtle.write("Game Over", align="center", font=("Verdana", 50, "normal"))
    print("Good game")
# run a game of hangman
def hangman(turtle, hangman_screen, answer, update_turtle, body_turtle):
    # initilize wrong_guesses variable and lists of guessed letters, letters in the word, and letters being displayed. Display gallows with underscores.
    wrong_guesses = 0
    guessed_letters = []
    answer_list = [i for i in answer]
    displayed_characters = ["_" for i in range(len(answer))]
    display_gallows(turtle, hangman_screen)
    update_gallows(displayed_characters, update_turtle)
    while True:
        # ask for letter guess until it's not a letter that has already been guessed
        letter_guess = input("Please guess a letter: ")
        while letter_guess in guessed_letters:
            letter_guess = input("Already guessed, guess again: ")
        guessed_letters.append(letter_guess)
        # if letter is in word, add it to display and erase underscore
        if letter_guess in answer_list:
            for pos, i in enumerate(answer_list):
                if i == letter_guess:
                    displayed_characters[pos] = i
                # if you guess all the letters, you win the game
                if "_" not in displayed_characters:
                    win_sequence(turtle, update_turtle, body_turtle)
            update_gallows(displayed_characters, update_turtle)
        # if letter is not in the word add one to wrong guesses and add a body part to the hangman
        else:
            wrong_guesses += 1
            # if you use up all your guesses, you lose, end game
            if wrong_guesses == 7:
                lose_sequence(turtle, update_turtle, body_turtle, answer)
                break
            add_body_part(wrong_guesses, body_turtle)
        # after every turn ask if they want to guess the word
        guess_word = input("Do you want to guess the word?(y/n) ")
        # if they want to, ask for the guess. If they don't, continue loop
        if (guess_word == 'y'):
            guessed_word = input("What's your guess? ")
            # if the guess is right, you win, update the screen
            if guessed_word == answer:
                displayed_characters = answer_list
                update_gallows(displayed_characters, update_turtle)
                win_sequence(turtle, update_turtle, body_turtle)
                break
            # if the guess is wrong, say it's wrong and continue the loop
            else:
                print("You guessed wrong!")
                continue
    # keep the hangman on the screen through each loop
    hangman_screen.mainloop()
def main():
    # initialize the turtles and hide them. Run hangman game.
    words = open("hangman.txt", "r")
    word = pick_random_word(words)
    turtle = trtl.Turtle()
    update_turtle = trtl.Turtle()
    body_turtle = trtl.Turtle()
    update_turtle.hideturtle()
    body_turtle.hideturtle()
    turtle.hideturtle()
    hangman_screen = trtl.Screen()
    hangman(turtle, hangman_screen, word, update_turtle, body_turtle)
if __name__ == "__main__":
    main()