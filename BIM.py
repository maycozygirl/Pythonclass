print("หาค่าดัชนีมวลกาย")
print("..............................................")
w = int (input ("enter your weigth"))
t = float (input (" enter your hight (cm)"))
t = t/100
BMI = w/(t**2)
print("your BMI is %.2f  " % BMI)

print("..............................................")
if BMI >= 18.50 and BMI <=22.90:
    print("สุขภาพดี\t\t\tปกติ")
elif BMI >= 23 and BMI <= 24.90:
    print("ท่วม\t\t\tอันตรายระดับ 1")
elif BMI >= 25 and BMI <= 29.90:
    print("อ้วน\t\t\tอันตรายระดับ 2")
elif BMI >=30:
    print("อ้วนมาก\t\t\tอันตรายระดับ 3")
print("...............................................")


#ปวีณ์ธิดา รอดฮวบ ม.4/comIT เลขที่ 25