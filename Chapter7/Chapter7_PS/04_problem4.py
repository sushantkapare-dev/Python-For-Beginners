#  Write a program to find whether a given number is prime or not. 

n = int(input("Enter a number: "))

for i in range(2 , n):
    if (n%2 == 0):
        print("The given number is Not Prime")
        break

else:
    print("The given number is Prime")
