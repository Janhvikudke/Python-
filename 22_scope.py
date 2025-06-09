def fun():
    x=20 #called local
    def ifun():
        print(x)
    ifun()
fun()

x=30 #called global
def fun():
    print(x)
fun()
print(x)

x = 40 #global
def func():
    x = 10 #local
    print(x)
func()
print(x)

def func():
  global x #using globle keyword
  x = 30
func()
print(x)

x = 35
def myfunc():
  global x
  x = 25 #change the variable value
myfunc()
print(x)