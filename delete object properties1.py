class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello"+self.name)
s1=students("John",35)
s2=students("David",36)
print(s1.name)
print(s1.age)
s1.myfunc()
del s1.age
print(s2.name)
print(s2.age)