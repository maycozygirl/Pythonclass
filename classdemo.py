class Student:
        def __init__(self):
            self.name = input("enter name : ")
            self.age = int(input("enter age : "))
        
        def setstudent(self):
            return (self.name)

stu = Student()

print(stu.setstudent)


