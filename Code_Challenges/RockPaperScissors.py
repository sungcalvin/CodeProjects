#This code generates a random number between 1 and 10, then asks the user to guess the number.  Will let user know if guess is too low, high, or exactly right.  Keeps track of guesses
#User can type "exit" to exit.
import random
a = random.randint(1, 10)
guesses = 0

while True:
    
    playerguess = int(input("Guess the number generated."))
    
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
        