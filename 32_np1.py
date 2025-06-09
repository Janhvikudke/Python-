import numpy as np

'''arr = np.array(1)
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
arr3 = np.array([[[1, 2],[3,4]], [[5, 6],[7,8]]])
print(arr.ndim,"dim",arr)
print("\n",arr1.ndim,"dim",arr1)
print("\n",arr2.ndim,"dim",arr2)
print("\n",arr3.ndim,"dim",arr3)
print("\n",np.__version__)'''

'''arr = np.array([1, 2, 3,4,5],ndmin=3)
print("\n",arr)
print("\n no of dimensions:",arr.ndim)'''

# indexing
'''a = np.array([1, 2, 3,4,5])
print(a[0])
print(a[1]+a[3])
print(a[-2])'''

'''b = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2dim:",b[0,2])
print("2dim",b[-1,-1])'''

'''c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3dim:",c[0,1,1])
print("3dim:",c[1,1,1])'''

# slicing
'''b = np.array([[1,2,3,4,5], [6,7,8,9,10]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(b[0,1:5:2])
print(b[1,::1])
print("c",c[0,1,0:2])
print("b",b[0:5,2:5])'''

# copy() and view()
'''a = np.array([1, 2, 3, 4, 5])
x = a.copy() #it's a copy of original,changes not accepted
y = a.view() #it's a view of original,changes accepted
a[0]=7
print(x)
print(y)
print(a)
print(x.base)
print(y.base)'''

# shape() and reshape()
'''a = np.array([[1,2,3,5],[5,4,3,2]])
print("shape of a",a.shape)
b = np.array([1,2,3,4,5,6,7,8],ndmin=3)
print(b)
print("shape of b",b.shape)
print(a.reshape(8)) # 2-D to 1-D
print(b.reshape(2,2,2)) 
print("reshape of a",a.reshape(-1))
print(a.reshape(1,2,-1))
#checking copy or view
print(b.reshape(1,2,4).base) #view'''

#iterating
'''a=np.array([2,4,6])
b=np.array([[1,3,5],[2,4,6]])
c=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in b:
    print(x)
for x in b:
  for y in x:
    print(y)
print()

for x in c:
   print(x)
for x in c:
  for y in x:
    for z in y:
      print(z)
print()

for x in np.nditer(b): 
  print(x) # using nditer()
print()

for x in np.nditer(a, flags=['buffered'], op_dtypes=['S']):
  print(x)
print()

for x in np.nditer(b[:, ::2]):
  print(x)
print()

for idx, x in np.ndenumerate(b):
  print(idx, x)'''

#joining
'''a=np.array([1,3,5])
b=np.array([2,4,6])
c=np.concatenate((a,b))
d=np.stack((a,b),axis=1) # transpose
print(c)
print(d)
print()

a = np.array([[1, 2], [3, 4]])
b= np.array([[5, 6], [7, 8]])
c = np.concatenate((a,b), axis=1)
d=np.stack((a,b))
print(d)
print(c)
print()

a=np.array([1,2,3])
b=np.array([6,7,8])
c=np.hstack((a,b)) #concate
print(c)
d = np.vstack((a, b))
print(d)
e = np.dstack((a, b))
print(e)'''

#splitting
'''a=np.array([1,3,5,7,9,11])
b=np.array_split(a,3)
c=np.array_split(a,4)
print(b)
print(c)
print(b[1])
print(b[2])

a=np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
b=np.array_split(a,3)
c=np.array_split(a,3,axis=1)
print(b)
print(c)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
b= np.hsplit(a,3)
print(b)'''
# vstack() and dstack() are available as vsplit() and dsplit()

# searching
'''a = np.array([1,1, 2, 3, 4, 5, 4, 4])
b = np.where(a == 4)
c=np.where(a%2 == 0)
print(b)
print(c)
d=np.searchsorted(a, 5)
e=np.searchsorted(a,5,side='right')
f=np.searchsorted(a, [2, 4, 6])
print(d)
print(e)
print(f)'''

#sorting
'''a=np.array([3,2,0,1])
b=np.array([[3, 2, 4], [5, 0, 1]])
c=np.array(['janhvi','anand','aditya'])
d=np.array([True,False,True])
print(np.sort(a))
print(np.sort(b))
print(np.sort(c))
print(np.sort(d))'''

#filtering
a=np.array([1,2,3,4,5])
b=[True,False,False,True,True]
c=a[b]
print(c)