l = [12 ,15,86,9,45,65,45]

# index = 0
# for item in l:
#     print(f"The item number at index{index } is {item}")
#     index += 1

# we can simplifies this by enumerate function

for index , item in enumerate(l):
    print(f"The item number at index{index } is {item}")

