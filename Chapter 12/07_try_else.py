try:
    a = int(input("Enter an number:"))
    print(a)

except Exception as e:
    print("Please enter a valid number")

else:
    print("I am inside an else ")