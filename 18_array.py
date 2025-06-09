arr=["varsha","janhvi","Kudke","More"]
print(len(arr))
print(arr[-1])
#1.append()
arr=["varsha","janhvi","Kudke","More"]
arr2=[8,6,4,2]
arr.append("7")
print(arr)
arr.append(arr2)
print(arr)
print()

#2.clear()
arr=["varsha","janhvi","Kudke","More"]
arr.clear()
print(arr)
print()

#3.copy()
arr=["janhvi","Kudke",'7','9']
arr2=arr.copy()
print(arr2)
# newlst=list(arr)
# print(newarr)
print()

#4.count()
arr=['2','4','6','8','4']
print(arr.count('4'))
print()

#5.extend()
arr=['2','4','6','8','4']
arr2=['1','3','5']
arr.extend('7')
print(arr)
arr.extend(arr2)
print(arr)
print()

#6.index()
arr=['2','4','6','8','4']
print(arr.index('8'))
print()

#7.insert()
arr=['2','4','6','8','4']
arr.insert(1,'7')
print(arr)
print()

#8.pop()
arr=['2','4','6','8','4','2']
arr.pop(2)
print(arr)
print()

#9.remove()
arr=['2','4','6','8','4']
arr.remove('4')
print(arr)
arr.remove('4')
print(arr)
print()

#10.reverse()
arr=[8,6,4,2,1,2]
arr.sort(reverse=True)
print(arr)
print()

#11.sort()
arr=["varsha","janhvi",'1','4',"Kudke","More"]
arr.sort()
print(arr)
