#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Homework 1
#Prints "welcome!" in different languages
lang_dict = {1: "Zoo siab txais tos!", 2: "Soo dhawoow!", 3: "Boozhoo!", 4: "Willkommen!"}
lang_choice = int(input("What language would you like to be greeted in?\nHmong:1\nSomali:2\nAnishinaabemowin:3\nGerman:4\n(Type corresponding number) "))
print(lang_dict[lang_choice])
