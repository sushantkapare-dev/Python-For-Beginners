try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as V:
    print("Heyyyy")
    print(V)

except Exception as e:
    print(e)

print("Thanks for using this code!")
