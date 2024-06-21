# Instance/Object attributes get preferance than class attributes during assignments.

class employee:
    language = "PY"     # This is class attribute
    salary = 5000

Rahul = employee()
Rahul.name = "Rahul" 
Rahul.language = "JAVA"     # This is an Instnace/object attribute
print(Rahul.name , Rahul.language , Rahul.salary)

