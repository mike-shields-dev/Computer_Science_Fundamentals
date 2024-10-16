import random

secret_number = random.randrange(1, 11)
guess = None

while(guess != secret_number):
    print("Enter a number between 1 and 10: ")
    
    try:
        guess = int(input())
    except ValueError:
        print("You did not enter an INTEGER!")
        guess = None
        continue
    
    if(guess != secret_number):
        print("Wrong! Try again!")
        
print("Correct!")
