# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

n = int(input("Enter the number : "))

table = [n*i for i in range(1 , 11)]
with open("table.txt", "a") as f:
    f.write(f"Multiplicatio table of {n}: {str(table)}\n")
