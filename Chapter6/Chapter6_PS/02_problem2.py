marks1 = int(input("Enter the marks of 1st subject: "))
marks2 = int(input("Enter the marks of 2nd subject: "))
marks3 = int(input("Enter the marks of 3rd subject: "))

# check the total percentage
total_percentage= (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and  marks1>=33 and marks2>=33 and marks3>=33):
    print("Congrats you are passed", total_percentage)

else:
    print("Sorry you are failed ", total_percentage)