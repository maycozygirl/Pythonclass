print("...................................")
name =  input("enter name")
lastname = input("enter lastname")
grade = float(input("enter aver grade"))
print("...................................")
if (grade >= 3.75 and grade <= 4.00):
   print("Faculty of medicine = %.2f  " % grade )
elif (grade >= 3.50 and grade <=4.00):
    print("Faculty of Dentists = %.2f  " % grade )
elif ( grade >= 3.00 and grade <= 4.00):
     print("Faculty of Engineering = %.2f  " % grade )
elif ( grade >= 2.50 and grade <= 2.99):
    print("Other faculty %.2f  " % grade )
elif (grade < 2.50):
    print(" you can't samak la %.2f " % grade )