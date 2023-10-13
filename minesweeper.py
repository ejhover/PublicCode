#Edabit challenge https://edabit.com/challenge/YDgtdP69Mn9pC73xN
def num_grid(minefield):
    mines = []
    shiftp = [-1, -1, -1, 0, 0, 1, 1, 1]#left to right line by line
    shiftq = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(len(minefield)):
        for j in range(len(minefield[i])):
            if minefield[i][j] == "-":
                minefield[i][j] = 0
            if minefield[i][j] == "#":
                mines.append([i, j])
    for pos, i in enumerate(mines):
        for pos2, j in enumerate(shiftp):
            if (mines[pos][0]+j > len(minefield)-1) or (mines[pos][0]+j < 0) or (mines[pos][1]+shiftq[pos2] > len(minefield[mines[pos][0]])-1) or (mines[pos][1]+shiftq[pos2] < 0):
                continue
            elif type(minefield[mines[pos][0]+j][mines[pos][1]+shiftq[pos2]]) == int:
                minefield[mines[pos][0]+j][mines[pos][1]+shiftq[pos2]] += 1 
    for pos, i in enumerate(minefield):
        for pos2, j in enumerate(minefield[pos]):
            if type(j) == int:
                minefield[pos][pos2] = str(j)
    return(minefield)



def main():
    print(num_grid(["#" for i in range(5) for j in range(5)]))
    '''
    print(num_grid([
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-']
]))'''

if __name__ == "__main__":
    main()
