password = "letmein"
guess = None

while(guess == None):
    print("Enter password: ")
    guess = input()
    
    if(guess != password):
        print("Incorrect password")
        guess = None

print("Access granted!")
        