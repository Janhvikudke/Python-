def hlo():
    print("hello from a function")
hlo()

def myname(name):
    print("my name is",name)
myname("janhvi")
myname("anand")

def myname(name1,name2):
    print(name1,name2)
myname("janhvi","kudke")
myname("anand","kudke")

def myname(*name):
    print("my surname is "+name[2])
    print("my name is "+name[0])
myname("janhvi","sakharam","kudke")

def myname(**name):
    print("my name is "+name["fname"])
myname(fname="janhvi",lname="kudke")

def myname(name="janhvi"):
    print("my name is "+name)
myname("anand")
myname("aditya")
myname()

def myname(name):
    for x in name:
        print(x)
names=("janhvi","aditya","anand")
myname(names)

def mul(x):
    return(3*x)
print(mul(1))
print(mul(2))
print(mul(3))

def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return(n*fact(n-1))
factorial=fact(0)
print(factorial)

def multi(x,y):
    print("multiplication",(x*y))
multi(3,3)
multi(5,5)
multi(7,7)

