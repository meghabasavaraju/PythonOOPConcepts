class car:
    wheels = 4 #class variable
    def __init__(self):
        self.mil =10
        self.com ="bmw"

# instance variables by default it is 10,and bmw i can change later
#inside the init if we declare it will become instance
# if we declare varibles inside class , it i called as class variables
c1=car()
c2=car()
car.wheels=2
c2.com='ferari'
print(c1.mil,c1.com)
print(c2.mil,c2.com)
print(c1.wheels)
