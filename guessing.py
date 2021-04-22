import random
number=random.randint(1,9)
chances=0
print("Guess a Number Between 1 and 9")
while chances<3: 
    guess=int(input("Enter Your Guess: "))
    if(guess==number):
        print("Congratulations! You guessed the number right!")
        break
    elif guess<number:
        print("Guess a higher number.")
    else: 
        print("Guess a lower number.")
    chances=chances+1
if not chances<3: 
    print("You lose.")