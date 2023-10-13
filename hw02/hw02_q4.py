#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Assignment 2

def print_multiplication_table():
    #Making columns
    for column in range(1, 10):
        #Making rows
        for row in range(1, 10):
            print(row+((column-1)*row), end='\t')
        #Start new line after each row
        print()
def main():
    print_multiplication_table()
if __name__ == "__main__":
    main()