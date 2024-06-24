# 2. Write a program to print third, fifth and seventh element from a list using enumerate function. 

l = [15, 45, 86  , 48 , 62 , 79 , 46]

for i , item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)