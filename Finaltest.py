class Dst:
        
        def __init__(self):
            self.speed = 0
            self.time = 0
            self.distance = 0
            self.chatacter = 0

        def Character(self):
            print("Character")
            print("Character D,d = Find Distance")
            print("Character T,t = Find Time")
            print("Character S,s = Find Speed")
            self.chatacter = (input("enter Character : "))
            if self.chatacter == "D" or self.chatacter == "d":
                stu.Distance() 
            elif self.chatacter == "S" or self.chatacter == "s":
                stu.Speed() 
            elif self.chatacter == "T" or self.chatacter == "t":
                stu.Time() 
            else: stu.Character()

        def Distance(self):
            self.speed =  float(input("enter speed (km/h): "))
            self.time =  float(input("enter time (h): "))
            self.time = (int(self.time) * 60 + ((self.time % 1)*100))/60
            self.distance = self.speed*self.time
            print ("Distance = %.2f"% self.distance ,"Km")
        
        def Speed(self):
            self.distance =  float(input("enter distance (km): "))
            self.time =  float(input("enter time (h) : "))
            self.time = (int(self.time) * 60 + ((self.time % 1)*100))/60
            self.speed = (self.distance/self.time)
            print ("Speed = %.2f"%self.speed,"Km/h")

        def Time(self):
            self.distance =  float(input("enter distance (km): "))
            self.speed =  float(input("enter speed (km/h): "))
            self.time = self.distance/self.speed 
            self.time = int(self.time) + (((self.time%1)/100)*60)
            print ("Time = %.2f"%self.time,"h")

    

stu = Dst()
stu.Character()

