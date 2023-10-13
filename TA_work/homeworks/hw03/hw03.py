import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C. 

# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose: Converts from celsius to fahrenheit
    Parameter(s): The number of degrees celsius that they would like to convert.
    Return Value: The given celsius measurement in fahrenheit.
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose: Print out 5 lines of 5 stars.
    Parameter(s): Nothing.
    Return Value: Nothing. 
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    

# Part B: ISBN Check Digit

def isbn_check(isbn):
    '''
    Purpose: Validate given ISBN numbers.
    Parameter(s): ISBN number.
    Return Value: Integar representing whether the ISBN number is real(0) or not (any other #).
    '''
    ans = 0
    for pos, i in enumerate(str(isbn)):
        if (pos%2)==0:
            ans+=(int(i))
        else:
            ans+=(3*int(i))
    return ans%10
# Part C: Who needs loops?

def print_121():
    list(map(lambda x: print("Who needs loops?"), range(121)))