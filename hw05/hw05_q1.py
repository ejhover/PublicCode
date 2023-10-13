# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Homework 5
# takes in letters which, after the application of the offset, go outside of the alphabet, and put them back inside
def outside_alph(num, offset):
    if not ((num - offset) >= ord("a")) and ((num-offset) <= ord("z")):
        return (chr(num-offset))
    if num < ord("a"):
        return chr((ord("z")+1) - (ord("a")-num))
    if num > ord("z"):
        return chr(((ord("a")-1) + num-ord("z")))
# adds an offset to a message letter by letter using recursion and prints offsetted message
def recursive_caesar(message, offset):
    message = message.lower()
    num = ord(message[0]) + offset
    if len(message) == 1:
        return chr(num) if ((message[0] != " ") and ((num >= ord("a")) and (num <= ord("z")))) else outside_alph(num, offset)
    else:
        return chr(num) + recursive_caesar(message[1:], offset) if ((message[0] != " ") and ((num >= ord("a")) and (num <= ord("z")))) else outside_alph(num, offset) + recursive_caesar(message[1:], offset)
# returns offsetted message but does it by halves of the original message
def muddled_caesar(message, offset):
    if len(message) < 1:
        return ""
    message1 = message[:len(message)//2].lower()
    message2 = message[len(message)//2:].lower()
    num1 = ord(message1[0]) + offset
    num2 = ord(message2[0]) + offset
    if len(message1) == 1:
        return chr(num1) if ((message[0] != " ") and ((num1 >= ord("a")) and (num1 <= ord("z")))) else outside_alph(num1, offset)
    else:
        return chr(num1) + recursive_caesar(message1[1:], offset) + " " + chr(num2) + recursive_caesar(message2[1:], offset) if ((message1[0] != " ") and (message2[0] != " ") and ((num1 >= ord("a")) and (num1 <= ord("z"))) and ((num2 >= ord("a")) and (num2 <= ord("z")))) else outside_alph(num1, offset) + recursive_caesar(message1[1:], offset) + " " + outside_alph(num2, offset) + recursive_caesar(message2[1:], offset)
# obtains the message and how much they want it offsetted and offset it the 2 different recursive ways
def main():
    message = input("Please enter your string: ")
    offset = int(input("Enter the offset: "))
    print("Regular decryption: ", recursive_caesar(message, offset))
    print("Muddled decryption: ", end="")
    print(muddled_caesar(message, offset))
if __name__ == "__main__":
    main()