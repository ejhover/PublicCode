def name_generator(adj, names):
    ans = []
    #check that there is input into the function
    if (len(adj) < 1) or (len(names) < 1):
        return("No name to print")
    else:
    #return every combination of adj and names 
        for i in adj:
            for j in names:
                ans.append(f'{i} {j}')
        return(ans)
def main():
    #getting input of strings and turning into a list
    adj = input("Enter list of adjectives separated by space: ").split()
    names = input("Enter list of names: ").split()
    print(name_generator(adj, names))

if __name__ == "__main__":
    main()

    