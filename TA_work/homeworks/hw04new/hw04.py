# 5 min
def sound(weight):
    if weight<13:
        return 'Yip'
    elif weight<=30:
        return 'Ruff'
    elif weight<=70:
        return 'Bark'
    else:
        return 'Boof'
# 5 min
def sound2(weight, is_cat):
    return sound(weight) if not is_cat else 'Meow'
# 10 min
def three_options(text, optionA, optionB, optionC):
    print(text)
    print(optionA + "\n" + optionB + "\n" + optionC)
    choice = input("Choose A, B, or C: ")
    while choice not in ['A', 'B', 'C']:
        print('Invalid option, try again.')
        choice = input("Which case? ")
    return choice
# 20 minutes
def adventure():
    first=three_options("What do you want? ", "AirPods", "Phone", "Computer")
    if first=='A':
        print("Good choice")
        return True
    elif first=='C':
        second = three_options("What kind do you want", "Windows", "Linux", "Mac")
        if second in ['A', 'B']:
            print("Great choice")
            return True
        elif second == 'C':
            print("bad choice")
            return False
    else:
        third = three_options("What kind do you want", "iPhone", "Android", "Google Pixel")
        if third in ['B', 'C']:
            print("bad choice")
            return False
        else:
            fourth = three_options("What accessory do you want?", "Pop socket", "Durable case", "fast charger")
            if fourth == 'A':
                print("What are you thinking")
                return False
            elif fourth == 'C':
                print("Great decision")
                return True
            else:
                another = three_options("What kind do you want", "Windows", "Linux", "Mac")
                if second in ['A', 'B']:
                    print("Great choice")
                    return True
                elif second == 'C':
                    print("bad choice")
                    return False



if __name__ == '__main__':
    # print(sound(6)) # Should output Yip
    # print(sound(30)) # Should output Bark
    # print(sound(31))
    # print(sound(80))
    # print(sound2(13, True)) # Should output Meow
    # print(sound2(50, False)) # Should output Bark
    # print(sound2(80, True))
    # print(sound2(20, False))
    # three_options("You must decide the fate of the galaxy.",
    #    "Destroy the robots",
    #    "Control the robots",
    #    "Merge with the robots?")