s_num = [] #เก็บตัวแปรได้หลายประเภท
#test_list[2] = "yyy" #เข้าไปเปลี่ยนในตัวแปรหลัก
Num = int(input("Enter student number"))

for x in range(Num):
    str = input("student name = ")
    s_num.append(str)
    print(s_num[x])