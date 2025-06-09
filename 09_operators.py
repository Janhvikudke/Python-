print("Arithmetic operators")
a=25
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
print()

print("Assignment operators")
c=25
print(c)
c+=10
print(c)
c-=10
print(c)
c*=10
print(c)
c/=10
print(c)
c%=10
print(c)
c//=10
print(c)
c**=10
print(c)
# c&=10
# print(c)
# c|=10
# print(c)
# c^=10
# print(c)
# c>>=10
# print(c)
# c<<=10
# print(c)
print()

print("Comparison Operators")
d=10
e=9
print(d==e)
print(d!=e)
print(d>e)
print(d<e)
print(d>=e)
print(d<=e)
print()

print("Logical Operators")
f=4
print(f<5 and f>3)
print(f==4 or f<2)
print(not(f<5))
print()

print("Identity operators")
g=("janhvi","anand","aditya")
h=("varsha","vishal","yogita")
i=("janhvi","anand","aditya")
h=g
print(g is i)
print(g is h)
print(g is not h)
print(g==h)
print(g==i)
print()

print("Membership Operators")
j=("janhvi","anand","aditya")
print("anand" in j)
print("kudke" not in j)
print("kudke" in j)
print()

print("Bitwise Operators")
k=7
l=9
m=12
n=1
'''
8 4 2 1 
0 1 1 1 ->7
1 0 0 1 ->9
1 1 0 0 ->12
1->true
0->false
'''
print(k&l) #and
# both are true
print(k|m) #or
# atleast one true
print(k^m) #xor
# only 1 true
print(~m)  #not
# (convert all bits) 
# add 1 and convert negative 
print(k<<5) #left shift
# add 0, 5 times to the right side
# 7*(2^5)
print(k>>2) #right shift
# add 0, 5 times to the left side
# 7/(2^5)
