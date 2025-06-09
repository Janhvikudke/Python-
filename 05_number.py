#print type of variable values
a=3
b=3.4
c=2j
print(type(a))
print(type(b))
print(type(c))

x=3.2e5
y=1.2E5
z=-4.6e5
print(type(x))
print(type(y))
print(type(z))

#convert type and stored another variable
p=2
q=3.3
r=5j

x=float(p)
y=int(q)
z=complex(q)
print(x)
print(y)
print(z)

#print random value using function
import random
print(random.randrange(1,15))
