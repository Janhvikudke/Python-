tup=("j","s","k")
print(tup)

tup2=("k",) #create one item in tuple using (,)
print(tup2)
print(type(tup2))
print()

tup=tuple(("j","s","l")) #using constructor
print(tup)
print()

print(tup[1]) #access item using index
print(tup[-1]) #negative index
print(tup[:3]) #range index
print()

#Update tuple
tup=("j","k","v","y","m")
print(tup)
lst=list(tup)
lst[2]="a"  #change specific element using index
tup=tuple(lst)
print(tup)
print()

tup=("j","k","v","y","m")
lst=list(tup)
lst.append("g") #add element at the end 
tup=tuple(lst)
print(tup)
print()

tup=("j","k","v","y","m")
tup2=("a",)
tup += tup2 #add 2 tuples using assignment operator
print(tup)
print()

#Unpacking tuple
tup=("j","k","v","m")
(g,y,r,p)=tup
print(g)
print(y)
print(r)
print(p)
print()

tup=("j","k","v","m","y","g")
(g,*y,r)=tup
print(g)
print(y)
print(r)
print()

# join 2 tuples
tup=("j","v","y")
tup1=("k","m","g")
tup2=tup+tup1
print(tup2)

# multiply tuple
tup=("j","v","y")
tup1=tup*3
print(tup1)
print()

# Methods
# 1.count
tup=("j","k","v","m","v","v")
print(tup.count("v"))

# 2.index
tup=("j","k","v","m","v","v")
print(tup.index("v"))

