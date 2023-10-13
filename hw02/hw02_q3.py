#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Assignment 2
def is_ginger_number(number):
    #List of the prime numbers to check with
    prime = [7, 5, 3, 2]
    counter = 0
    while number != 1:
        #If you loop through all the numbers in the list, leave the loop and return T or F
        if counter > 3:
            break
        if (number % prime[counter])==0:
            number/=prime[counter]
        else:
            counter+=1
            continue
    if number != 1:
        return False
    else:
        return True
def main():
    num = int(input("Enter number: "))
    print(is_ginger_number(num))
if __name__ == "__main__":
    main()
