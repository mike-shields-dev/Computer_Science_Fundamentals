result = 1
counter = 2
limit = None

while(limit == None):
    print("Enter an integer to find its factorial")
    try:
        limit = int(input())
    except ValueError: 
        print("You did not enter an integer!")
        continue

while(counter <= limit):
    result *= counter
    counter += 1
    
print(f"{ limit }! = { result }")
