# Write a python program using function to convert Celsius to Fahrenheit. 

def celsius_to_fahrenheit(f):
    return 5*(f-32)/9

f = int(input("Enter the temperature in fahrenheit: "))
c = celsius_to_fahrenheit(f)
print(f"{round(c , 2)}°C")

