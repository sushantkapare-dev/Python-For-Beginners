marks = {
    "Rahul": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "sush"
    
}

print(marks.items())   # List down all the key-value pair
print(marks.keys())    # List down all the key pairs
print(marks.values())  # List down all the values pairs
marks.update({"Rahul": 99 , "Amit": 65})   # Udate and add new key value pair
print(marks.get("Akash"))    # Prints none
print(marks["Akash"])        # It returns Error



