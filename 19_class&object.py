'''
class Myclass:
    x=7
p1=Myclass()
print(p1.x)
'''
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

x1=Person("janhvi",21)

print(x1.name)
print(x1.age)
print(x1)
'''
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"

x1=Person("janhvi",21)
print(x1)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(x):
        print("my name",x.name)

x1=Person("janhvi",21)
x1.myfun()
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(x):
        print("my name",x.name)

x1=Person("janhvi",21)
x1.name="anand"
x1.myfun()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(x):
        print("my name",x.name)

x1=Person("janhvi",21)
# del x1.name
x1.name
