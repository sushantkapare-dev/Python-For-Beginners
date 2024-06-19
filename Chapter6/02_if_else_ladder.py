a = int(input("Enter your age: "))

if(a>=18):
    print("You are eligible to vote")

elif(a<0):
    print("Age cannot be negative")

elif(a==0):
    print("You were just born")

else:
    print("You are not eligible to vote")

print("Thank you for using our system")