# Write a program using functions to find greatest of three numbers. 

def gretest(a , b , c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 1
b = 45
c = 63

print(gretest(a, b, c))
