class computer:
    def __init__(self,cpu,ram):
        self.c = cpu
        self.r = ram
    def config(self):
        print("configuration is: ", self.c,self.r)
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        s3= student(m1,m2)
        return s3
    def __str__(self):
        return f"{self.m1} {self.m2}"
        

com1 = computer("i5", 8)
com2 = computer("i7", 16)

com1.config()
com2.config()

s1 = student(10,20)
s2 = student(20,30)

s3 = s1+s2
print(s3)