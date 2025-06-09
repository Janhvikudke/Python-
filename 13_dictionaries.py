dict1={'jani':'co','yogi':'entc','yogi':'entc','varsu':'pharma'}
print(dict1)
print()

print(len(dict1)) # len()
print(type(dict1)) # type()
print(dict1["jani"]) # return value
print()

# multi values stored in single key
dict2={"jani":"co","yogi":"entc",
"int":[1,2,3],
"char":('x','y','z')}
print(dict2)
print()

# using constructor()
dict3=dict(jani="co",yogi="entc")
print(dict3)
# TypeError: 'dict' object is not callable
print()

print(dict2["jani"])
print()

# 1.get(),return value
A=dict2.get("yogi")
print(A)
print()

# 2.keys()
print(dict2.keys())
print()

# 3.values()
print(dict2.values())
print()

# 4.items()
print(dict2.items())
print()

# 5.fromkeys()
A=dict.fromkeys(dict2,"co")
print("fromkeys",A)
print()

# 6.setdefault()
A=dict2.setdefault("yogi","co")
# value is optional(if key is present)
# if key doen't present then value become key
print(A)
print()

# add new pair
print("dict1",dict1)
dict1["varsu"]="pharma"
print(dict1)
print()
# checking present or not
if "janhvi" in dict1:
    print("present")
print()

# 7.update(),update value using function
dict1.update({"varsu":"pharmaa"})
print(dict1)
# update value
dict1["varsu"]="gore"
print(dict1)
print()

# 8.pop()
dict1.pop("varsu") #1 argument needed
print(dict1)
print()

# 9.popitem()
dict1.popitem() #this method remove last pair
print(dict1)
print()

dict1={'jani':'co','yogi':'entc','varsu':'pharma'}
# 10.del()
del dict1["varsu"] #delete specific pair
print(dict1)
# del dict1     #delete dictionary
# print (dict1)
print()

# 11.copy()
dicti=dict1.copy()
print(dicti)
# dict()
dicti=dict(dict1) #copy dictionary using dict()
print(dicti)
print()

# 12.clear()
dict1.clear()
print(dict1)
print()

# nested dict
we_3={
    "no1":{
        "name":"janhvi",
      "branch":"co"
    },
    "no2":{
        "name":"anand",
      "branch":"co"
    },
    "no3":{
        "name":"aditya",
      "branch":"entc"
    }
}

print(we_3["no1"])
print()
print(we_3["no1"]["name"])
print()

no1={
      "name":"janhvi",
    "branch":"co"
    }
no2={
      "name":"anand",
    "branch":"co"
    }
no3={
      "name":"aditya",
    "branch":"entc"
    }
we_3={
  "no1":no1,
  "no2":no2,
  "no3":no3
}
print(we_3.keys())
print(we_3["no2"]["branch"])