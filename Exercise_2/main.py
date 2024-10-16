import datetime

user_date_of_birth = None

while ( user_date_of_birth == None):
    print("Hello there user! I would like to calculate your age. Please can you tell me the YEAR you were born?")
    
    try:
        user_date_of_birth = int(input())
    
    except ValueError:
        print("You did not enter an integer!")
        continue
    
    if user_date_of_birth > datetime.datetime.now().year:
        print("Please provide a YEAR that is less than or equal to the current year.")
        user_date_of_birth = None

user_age = datetime.datetime.now().year - user_date_of_birth

print(f"You are {user_age} years old")
