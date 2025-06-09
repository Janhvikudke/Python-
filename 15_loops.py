no=int(input("enter the no: "))

i=0          # ->initialization
while(i<no): # ->condition
    i+=1     # ->incre/decre
    print(i) # ->return value
print()

# break statement(after print)
a=5
while a>=1:
    print(a)
    if a==3:
        break
    a-=1
print()

# break statement(before print)
a=5
while a>=1:
    if a==3:
        break
    print(a)
    a-=1
print()

# continue statement(before print)
a=5
while a>=1:
    a-=1
    if a==3:
        continue
    print(a)
print()

a=5
while a>=1:
    print(a)
    a-=1
else:
    print("loop is end")
print()

names=("janhvi","yogita","vishal")
for x in names:
    print(x)
for x in "janhvi":
    print(x)
    
# break statement(after print)
names=("janhvi","yogita","vishal")
for x in names:
    print(x)
    if x=="yogita":
        break
print()

# break statement(before print)
for x in names:
    if x=="yogita":
        break
    print(x)
print()

# continue statement(before print)
for x in names:
    if x=="yogita":
        continue
    print(x)
print()

for i in range(3): #default starting 0 (0-2)
    print(i)
for i in range(2,6,2): #default increment 1
    print(i,"2,6,2")
print() 

#else in for loop
for x in range(7):
    if x==3:
        break
        print(x)
    else:
        print("finished!")
print()

#nested loop
for i in range(0,4):
    for j in range(0,i):
        print(i,end=" ")
    print()

a=('j','k','l')
b=(1,2,3)
for i in a:
    for j in b:
        print(i,j)


for i in range(0,no): # ->(start, end, incr/decr)
    if i%2==0:        # ->condition
        print(i,"-> no is even") # ->return value
    else:
        print(i,"-> no is odd")  # ->return value

'''i=0

while(i<no):
    i+=1
    print(i)'''
    