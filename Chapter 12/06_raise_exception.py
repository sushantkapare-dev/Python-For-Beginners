a = int(input("Enter an first number: "))
b = int(input("Enter an second number: "))

if ( b ==0 ):
    raise ZeroDivisionError("Division by zero is not allowed")

else:
    print(f"The devision if a/b is {a/b}")