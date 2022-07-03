#class is a blue print or templete
# things or stuff that i can put inside the class
# attributes -> variables
# behaviour -> methods(functions)

class bird:
    species='egglayers'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fly(self):
        print('im',self.name,"I can fly")

blu = bird('blu',6)
woo =bird('woo',12)
blu.fly()
print(type(blu))