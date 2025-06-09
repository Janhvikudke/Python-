lst=["j","y","j","a","n"]
print(lst)
print()

print(len(lst)) #len()
print(type(lst)) #type()
print()

#list() constructor
a=list(("j","y","j","a","n"))
print(a)
print()

print(lst[1]) #index
print(lst[1:3]) #range
print(lst[-1])  #negative
print()

print("yogita" in lst)
print("yogita" not in lst)

if "yogita" in lst:#in(check if item present)
    print("Yes") 
else:
    print("No")
print()

#change items
lst[2]=3
print(lst) 
lst[3:5]="v","m"
print(lst)
lst[1:2]=[1,2]
print(lst)
lst[3:5]=["v"]
print(lst)
print()

# insert() items
lst.insert(4,"a")
print(lst)
lst.insert(5,"d")
print(lst)
print()

#append() items
lst.append("a")
print(lst)
lst.append(10)
print(lst)
print()

#remove() items
lst.remove("d")
print(lst)
print()

#pop()
lst.pop()
print(lst)
lst.pop(5)
print(lst)
print()

#del()
del lst[4]
print(lst)
#del lst
#print(lst)
print()

#clear()
lst.clear()
print(lst)
print()

#Comprehension
lst=["j","y","k","g"]
newlst=[]
for x in lst:
    if "k" in x:
        newlst.append(x)
print(newlst)
#or
newlst=[x for x in lst if "k" in x]
print(newlst)
newlst=[x for x in lst if x!= "g"]
print(newlst)
print()

#Iterable
newlst=[x for x in range(7)] 
print(newlst)
newlst=[x for x in range (7) if x<5]
print(newlst)
print()

#Expression
newlst=[x.upper() for x in lst]
print(newlst)
newlst=['janiii' for x in lst]
print(newlst)
newlst=[x if x!="ghule" else "anand" for x in lst]
print(newlst)
print()

#join 2 lists
lst=["janhvi","Kudke"]
lst2=[4,2]
lst3=[1.3,4.7]
list=lst+lst2+lst3
print(list)
print()

print("list_methods")
#1.append()
lst=["varsha","janhvi","Kudke","More"]
lst2=[8,6,4,2]
lst.append("7")
print(lst)
lst.append(lst2)
print(lst)
print()

#2.clear()
lst=["varsha","janhvi","Kudke","More"]
lst.clear()
print(lst)
print()

#3.copy()
lst=["janhvi","Kudke",'7','9']
lst2=lst.copy()
print(lst2)
# newlst=list(lst)
# print(newlst)
print()

#4.count()
lst=['2','4','6','8','4']
print(lst.count('4'))
print()

#5.extend()
lst=['2','4','6','8','4']
lst2=['1','3','5']
lst.extend('7')
print(lst)
lst.extend(lst2)
print(lst)
print()

#6.index()
lst=['2','4','6','8','4']
print(lst.index('8'))
print()

#7.insert()
lst=['2','4','6','8','4']
lst.insert(1,'7')
print(lst)
print()

#8.pop()
lst=['2','4','6','8','4','2']
lst.pop(2)
print(lst)
print()

#9.remove()
lst=['2','4','6','8','4']
lst.remove('4')
print(lst)
lst.remove('4')
print(lst)
print()

#10.reverse()
lst=[8,6,4,2,1,2]
lst.sort(reverse=True)
print(lst)
print()

#11.sort()
lst=["varsha","janhvi",'1','4',"Kudke","More"]
lst.sort()
print(lst)

print(len(lst)-1)
print(lst[len(lst)-1])