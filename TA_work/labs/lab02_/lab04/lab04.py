import turtle
turtle.speed(0)
def letters(digit):
    if (digit == 1) or (digit == 2) or (digit == 6):
        return 3
    elif (digit == 4) or (digit == 5) or (digit == 9):
        return 4
    else:
        return 5
def most_letters(num1, num2, num3):
    return "Tied!" if ((letters(num1)==letters(num2)) or (letters(num1)==letters(num3)) or (letters(num2)==letters(num3))) else num1 if letters(num1)==max(letters(num1), letters(num2), letters(num3)) else num2 if letters(num2)==max(letters(num1), letters(num2), letters(num3)) else num3 if letters(num3)==max(letters(num1), letters(num2), letters(num3)) else 0
def choose_rb():
    choice, limit = input("Choose Red or Blue: "), 0
    while choice != 'Red' and choice != 'Blue':
        limit+=1
        if limit==5:
            choice='Blue'
            break
        print(f'{choice} is not one of the valid options.')
        choice = input("Choose Red or Blue: ")
    return choice

def draw_square(length):
    i = 0
    while i < 4:
        turtle.fd(length)
        i+=1
        turtle.left(90)

'''
Explain what causes each error below.
See the instructions for descriptions of each error:

Syntax Error 1: the line above was indented too much
Runtime Error 1: you didn't ask for an input()
Runtime Error 2: they used equals instead of the = assignment
Logic Error 1: should be while j<num
Runtime Error 3: length was in quotes
Logic Error 2: turtle.left was outside of the while loop
Logic Error 3: i+=1 instead of i+1
'''
def zeller(month, day, year):
    old_month = month
    old_year = year
    if (month == 1) or (month == 2):
        year -= 1
        month += 12
    ans = ((day + 5 + ((26*(month+1))//10) + ((5*(year%100))//4) + ((21*(year//100))//4))%7)
    weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    return("{}/{}/{} is a {}".format(old_month, day, old_year, weekdays[ans]))


if __name__ == '__main__':
    # month = int(input("What is the month? "))
    # day = int(input("What is the day? "))
    # year = int(input("What is the year? "))
    # print(zeller(month, day, year))
    # num = int(input("Enter the number of squares: "))
    # size = int(input("Enter the side length: "))
    # j = 0
    # while j < num:
    #     draw_square(size)
    #     turtle.left(360/num)
    #     j += 1
    # turtle.exitonclick()
    # print(choose_rb())
    # print(letters(2)) #Should output 3
    # print(letters(7)) #Should output 5
    # print(letters(5)) #Should output 4
    # print(most_letters(6, 3, 2))
