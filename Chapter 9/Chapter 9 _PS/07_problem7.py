# Write a program to find out the line number where python is present from Question 6. 

with open("log.txt") as f :
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
        print(f"Python is present on line number: {lineno}")
        break
    lineno = lineno + 1

else:
    print("Python is not present in the file")
