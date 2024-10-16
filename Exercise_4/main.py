celsius = None

while(celsius == None):
    print("Enter a temperature in degrees Celsius: ")
    
    try:
        celsius = float(input())
    except ValueError:
        print("You did not enter a NUMERIC value. Please try again.")
        celsius = None
        
fahrenheit = celsius * 9/5 + 32

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
