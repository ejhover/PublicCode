#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Assignment 2
def sum_thirds(n):
    thirds_counter = 0
    #For all the pos numbers under the input 'n' that are divisible by 3, add one to the counter.
    for i in range(n):
        if (i%3) == 0:
            thirds_counter += i
    #Return counter
    return(thirds_counter)
def get_user_input():
    return(int(input("Enter number: ")))
def main():
    #Get user input
    print(sum_thirds(get_user_input()))
if __name__ == "__main__":
    main()
