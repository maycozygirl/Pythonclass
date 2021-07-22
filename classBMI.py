print("หาค่าดัชนีมวลกาย")
print("..............................................")

class bmi:
    def __init__(self):
        self.name = input("enter name : ")
        self.age = int(input("enter age : "))
        self.w = int (input ("enter your weigth (kg) : "))
        self.t= float (input ("enter your hight (cm) : ")) 

    def calbmi(self):
        self.w
        self.t
        self.t = self.t/100
        self.BMI = self.w/(self.t**2)
        print("your BMI is %.2f  " % self.BMI)
        return self.BMI
  
    def bmi (self):
        self.BMI
        if self.BMI >= 18.50 and self.BMI <=22.90:
            print("สุขภาพดี\t\t\tปกติ")
        elif self.BMI >= 23 and self.BMI <= 24.90:
            print("ท่วม\t\t\tอันตรายระดับ 1")
        elif self.BMI >= 25 and self.BMI <= 29.90:
            print("อ้วน\t\t\tอันตรายระดับ 2")
        elif self.BMI >=30:
            print("อ้วนมาก\t\t\tอันตรายระดับ 3")


stu = bmi()
stu.calbmi()
stu.bmi()
print("..............................................")
