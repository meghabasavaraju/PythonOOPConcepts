#there are 3 types of methods
#class method
#instatnce method
#static method
class student:
    school="TechieMonk"
    def __init__(self,M1,M2,M3):
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
    def avg(self): #instance Method cause it works with objects
        #two types of Methods
        #Accessor Methods
        #Mutator Methods
        return (self.M1+self.M2+self.M3)/3
    def get_M1(self):  #Accessor cause it fetch the variables
        return self.M1
    def set_M1(self,value):
        self.M1= value #mutator caue it updates the value of a variables
    #if you are working with object variables use self
    #if you are working with class variables use cls
    # if you are creating a alss method you have to use decorator @classmetho
    @classmethod
    def info(cls):
        cls.school="techieMonkPvt"
        return cls.school

    # when you are not concerned about neither class var or object var
    # will go for static variable
    # for static variable we will use decorator @staticmethod
    @staticmethod
    def infow():
        print("hello, welcome to techieMonk")
s1=student(25,24,23)
s2=student(19,23,21)
s3=student(18,21,25)
print(s1.avg())
print(s2.avg())
print(s3.avg())
print(s1.info())
print(student.info())
student.infow()
s1.infow()