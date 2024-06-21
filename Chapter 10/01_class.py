class employee:
    language = "PY"     # This is class attribute
    salary = 5000

Rahul = employee()
Rahul.name = "Rahul"      # This is an object attribute
print(Rahul.name , Rahul.language , Rahul.salary)

Sam = employee()
Sam.name = "Sam"
print( Sam.name , Sam.salary , Sam.language )


# Here name is instance attribute and  
# salary and language are class attributes as they directly belong to the class
