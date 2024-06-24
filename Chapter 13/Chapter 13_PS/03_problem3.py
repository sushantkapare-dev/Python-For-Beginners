'''
3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers. 

    7 
    14
    21
    ...
'''

table = [str( 7 * i) for i in range(1, 11)]

vertical_table = "\n".join(table)
print(vertical_table)