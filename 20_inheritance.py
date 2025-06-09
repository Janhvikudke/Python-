'''
class Parent:
    def __init__(x,name,surname):
        x.name=name
        x.surname=surname
    def ns(y):
        print(y.name,y.surname)
class Child(Parent):
    pass #you can create empty class using pass
z=Parent("vandana","kudke")
z.ns()
z=Child("janhvi","kudke")
z.ns()
'''
'''
class Parent:
    def __init__(x,name,surname):
        x.name=name
        x.surname=surname
    def ns(y):
        print(y.name,y.surname)
class Child(Parent):
    def __init__(x,name,surname):
        Parent.__init__(x,name,surname)
z=Parent("vandana","kudke")
z.ns()
z=Child("janhvi","kudke")
z.ns()
'''
'''
class Parent:
    def __init__(x,name,surname):
        x.name=name
        x.surname=surname
    def ns(y):
        print(y.name,y.surname)
class Child(Parent):
    def __init__(x,name,surname):
        super().__init__(name,surname)
z=Parent("vandana","kudke")
z.ns()
z=Child("janhvi","kudke")
z.ns()
'''
'''
class Parent:
    def __init__(x,name,surname):
        x.name=name
        x.surname=surname
    def ns(y):
        print(y.name,y.surname)
class Child(Parent):
    def __init__(x,name,middle,surname):
        super().__init__(name,surname)
        x.middle=middle
z=Parent("vandana","kudke")
z.ns()
z=Child("janhvi","sakharam","kudke")
print(z.middle)
'''
class Parent:
    def __init__(x,name,surname):
        x.name=name
        x.surname=surname
    def ns(y):
        print(y.name,y.surname)
class Child(Parent):
    def __init__(x,name,middle,surname):
        super().__init__(name,surname)
        x.middle=middle

    def hlo(y):
        print("hlo, my name is",y.surname, y.name, y.middle)
z=Parent("vandana","kudke")
z.ns()
z=Child("janhvi","sakharam","kudke")
print(z.name)
z.hlo()