a1= int(input("Enter an number 1: "))
a2= int(input("Enter an number 2: "))
a3= int(input("Enter an number 3: "))
a4= int(input("Enter an number 4: "))

if (a1>a2 and a1>a3 and a1>a4):
    print("Number 1 is greater", a1)

elif (a2>a1 and a2>a3 and a2>a4):
    print("Number 2 is greater", a2)

elif (a3>a1 and a3>a2 and a3>a4):
    print("Number 3 is greater", a3)

else:
    print("Number 4 is greater", a4)