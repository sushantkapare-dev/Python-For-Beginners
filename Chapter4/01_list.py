demo = ["Rahul", "Ajinkya", 5 ,53695.26 ,"Akash"]

print(demo[0])
demo[0] = " Starbucks"  # Unlike strings list are mutable

print(demo[0])
print(demo[-3])  # Negative indexing
print(demo[1:4])  # Slicing
demo[2] = "Vijay"  # Lists are mutable
print(demo)