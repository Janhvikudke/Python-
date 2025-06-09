x=lambda a:a+15
print(x(7))

x=lambda a,b:a*b
print(x(4,6))

x=lambda a,b,c:a+b+c
print(x(4,6,7))

def myfun(n):
    return lambda x:x*n

double=myfun(2)
triple=myfun(3)

print(double(7))
print(triple(7))