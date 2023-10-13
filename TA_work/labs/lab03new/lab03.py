import turtle
turtle.speed(0) #Change this to 0 to speed up the turtle
# Warm-up: 5 min
# Stretch: 5 min
# Workout: 6 min
def triangle(side):
    '''
    Purpose: Draws an equilateral triangle
    Parameter:
        side - (int) Length for each side of the triangle
    Return Value: None
    '''
    turtle.forward(side) #Move forward
    turtle.left(120) #Turn 120 degrees
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)

def triforce(side):
    triangle(side//2)
    turtle.forward(side) 
    turtle.left(120)
    triangle(side//2)
    turtle.forward(side)
    turtle.left(120)
    triangle(side//2)
    turtle.forward(side)
    turtle.left(120)
def triception(side):
    triforce(side//2)
    turtle.forward(side) 
    turtle.left(120)
    triforce(side//2)
    turtle.forward(side)
    turtle.left(120)
    triforce(side//2)
    turtle.forward(side)
    turtle.left(120)

def print_endsum(val):
    '''
    Purpose: Computes the sum of the first and last digits of an integer
    Parameter:
    val - (int) Positive integer we’re getting the digits from
    Return Value: None
    '''

    sval = str(val)
    first = sval[0]
    last = sval[len(sval)-1]
    print(int(first) + int(last))
def return_endsum(val):
    '''
    Purpose: Computes the sum of the first and last digits of an integer
    Parameter:
    val - (int) Positive integer we’re getting the digits from
    Return Value: (int) Sum of the first and last digits of val
    '''
    sval = str(val)
    first = sval[0]
    last = sval[len(sval)-1]
    return(int(first) + int(last))

def anonymize(username, domain):
    '''
    Purpose: Anonymize a given email
    Parameter(s): 
    username - the username of an email before the domain
    domain - the domain of the given email (everything after the username)
    Return Value: The full anonymized email
    '''
    return username[0]+'*****'+username[-1]+domain