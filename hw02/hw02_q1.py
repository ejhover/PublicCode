#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Assignment 2
import random
def magic_response():
   '''a function that returns one of the preset responses by random'''
   responses = [
   "As I see it, yes.",
   "Ask again later.",
   "Better not tell you now.",
   "Cannot predict now.",
   "Concentrate and ask again.",
   "Don definitely.",
   "You may rely on it."
   ]
   return random.choice(responses)
def main():
   #Loop and continue printing responses until 'goodbye' is typed
   while True:
      response = input("What would you like to ask the Magic 8-Ball? ")
      if response == "goodbye":
         break
      else:
         print(magic_response())
if __name__ == "__main__":
    main()
