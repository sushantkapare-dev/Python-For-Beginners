'''
4. Write a program to display a/b where a and b are integers. 
If b=0, display infinite by handling the ‘ZeroDivisionError’.
'''


try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a/b)

except ZeroDivisionError as V:
    print(V)
    print("Infinite")




