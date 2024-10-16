sum = 0
user_input = None

print("Enter a number: ")

while(user_input != 0):
    try:
        user_input = float(input())
    except ValueError: 
        print("You did not enter a numeric value!")
        user_input = None
        continue
        
    if(user_input != 0):
        sum += user_input
    else:
        print(f"Total sum: { sum }")    
