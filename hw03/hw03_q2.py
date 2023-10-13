def check_diagonal(matri):
    #checks if input is long enough to check diagonal on
    if len(matri) < 2:
        return None
    #iterate through every value down the diagonal and check it's equal to 1
    for i in range(len(matri)):
        if matri[i][i] == 1:
            continue
        #if the diagonal breaks and is not 1 then return False that there is no diagonal
        else:
            return False
            break
    return True
def main():
    matri = []
    #getting the list input and turning into matrix
    length = int(input("How many rows in your list: "))
    for i in range(length):
        row = (input("input row numbers separated by spaces: ")).split()
        matri.append(row)
    for i in range(len(matri)):
        for j in range(len(matri[i])):
            matri[i][j] = int(matri[i][j])
    print(check_diagonal(matri))
if __name__ == "__main__":
    main()