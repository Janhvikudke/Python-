set_A={11,12,14,15}
set_B={1,2,11,15}

for x in set_A:
    print(x)
print(11 in set_B)

# 1.add()
set_B.add(7)
print("add->7",set_B)

# 2.update()
set_B.update(set_A)
print("update->",set_B)

lst=['a','b','c']
tup=('x','y','z')
set_B.update(lst)
print("added list",set_B)
set_A.update(tup)
print("added tuple",set_A)

# 3.remove()
set_A={11,12,14,15,16}
set_B={1,2,7,11,15}
set_A.remove(11)
print("remove->11",set_A)

# 4.discard()
set_A.discard(12)
print("discard->x",set_A)

# 5.pop()
set_A.pop()
print("remove using pop",set_A)

# 6.clear()
set_A.clear()
print("clear set",set_A)

# 7.del
'''del set_A
print(set_A)'''

# 8.copy()
set_D=set_B.copy()
print("copy set_B",set_D)
print()

set_A={11,12,14,15,16}
set_B={1,2,7,11,15}
# 9.union()
set_C=set_A.union(set_B)
print("union->",set_C)
print("union(|)",set_A|set_B)
print()

# 10.difference()
set_C=set_A.difference(set_B)
print("different->",set_C)
print("different(-)",set_B-set_A)

# 11.difference_update()
set_B.difference_update(set_A)
print(set_B)
print()

set_A={11,12,14,15,16}
set_B={1,2,7,11,15}
# 12.intersection()
set_C=set_A.intersection(set_B)
print("intersect items->",set_C)
print("intersect items(&)",set_A&set_B)

# 13.intersection_update()
set_A.intersection_update(set_B)
print(set_A)
print()

set_A={11,12,14,15,16}
set_B={1,2,7,11,15}
# 14.symmetric_difference()
set_C=set_A.symmetric_difference(set_B)
print("same items remove->",set_C)
print("same items remove->",set_A^set_B)

# 15.symmetric_difference_update()
set_A.symmetric_difference_update(set_B)
print(set_A)
print()

set_A={12,14,2,16}
set_B={1,2,7,11,15}
# 16.isdisjoint()
set_C=set_A.isdisjoint(set_B)
# both set have unique items(not same)
print(set_C)

set_A={1,2,3,4}
set_B={1,2,3,4,5}
# 17.issubset()
set_C=set_A.issubset(set_B)
# all items in setA are present in setB
print(set_C)

# 18.issuperset()
set_C=set_A.issuperset(set_B)
# all items in setB are present in setA 
print(set_C)

'''
print(set_A|set_B) union
print(set_A-set_B) difference
print(set_A&set_B) intersection
print(set_A^set_B) symmetric difference
'''
