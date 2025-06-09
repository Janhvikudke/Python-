import json
a='{"name":"janhvi","city":"beed","age":20}'
print (a)
b=json.loads(a) #convert json to python
print(b)
print(b["age"])

c=json.dumps(b) #convert python to json
print(c)

c={"name":"janhvi",
"age": 20,
"brothers":("anand","aditya"),
"parents":[{"father":"sakharam"},
{"mother":"vandana"}]}
print(json.dumps(c,indent=4))
print(json.dumps(c,indent=4,separators=(":" "=")))
print(json.dumps(c,indent=4, sort_keys=True))