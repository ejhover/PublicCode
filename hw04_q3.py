# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Assignment 4

# Remove lines with less than 4 words, lowercase the lines, and return the list
def clean(pathname):
    f = open(pathname, 'r', encoding='utf-8')
    words = f.read().split("\n")

    for pos, i in enumerate(words):
        words[pos] = i.lower()
        if len(i.split(" ")) < 4:
            del words[pos]
    return(words)
    

# clean a file and then modify it for ever instance of "seven" change it to the number 7 
def replace_sevens(pathname):
    line_list = clean(pathname)
    new_list = []
    story_string = ""
    for pos, i in enumerate(line_list):
        new_list.append(i.split(" "))
    for pos, i in enumerate(new_list):
        for pos2, j in enumerate(i):
            if j.lower() == "seven":
                new_list[pos][pos2] = 7
    for i in new_list:
        for j in i:
            story_string += (str(j) + " ")

    new_file = open(pathname + '_modified.txt', 'w')
    new_file.write(story_string)
    new_file.close()
    
def main():
    clean("homeworks/hw04/data/short_stories.txt")
    replace_sevens("homeworks/hw04/data/short_stories.txt")
if __name__ == "__main__":
    main()