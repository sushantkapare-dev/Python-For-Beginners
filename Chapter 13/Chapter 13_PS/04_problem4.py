# 4. Write a program to filter a list of numbers which are divisible by 5. 

def devisible5(n):
    if (n%5 == 0):
        return True
    else:
        return False
    
a = [1 , 15 , 456, 45, 545 ,46, 7334, 444, 55, 80]

f = list(filter(devisible5 , a))
print(f)