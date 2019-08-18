#This code generates a random number between 1 and 10, then asks the user to guess the number.  Will let user know if guess is too low, high, or exactly right.  Keeps track of guesses
#User can type "exit" to exit.
import random
lownumber = 1
highnumber = 10
a = random.randint(lownumber, highnumber)
guesses = 0

print("There is a number between ", lownumber, "and ", highnumber, ".")

while True:
    
    playerguess = int(input("Guess the number generated in between."))
    
    if playerguess == a:
        print("You got the number!")
        print("You took ", guesses, "guesses to arrive at the answer!")
        break
        
    elif playerguess < a:
        print("Too little! Guess again!")
        guesses = guesses + 1
        
    elif playerguess > a: 
        print("Too high! Guess again!")
        guesses = guesses + 1

    elif playerguess == "exit":
        break
        
    else:
        print("Not a number!  Guess again!")
        