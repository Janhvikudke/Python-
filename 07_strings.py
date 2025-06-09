#multiline string print 
a="""hlo,
my name is janhvi and,
i'm diploma pass out student"""
print(a)

b='''hlo,
my name is janhvi and,
i'm diploma pass out student'''
print(b)

#index value print
a="hello"
print(a[1])

#each element print single line
for i in "banana":
    print(i)

#print length of string
a=("anand","aditya","vishal")
print(len(a))

#check string print true/false 
a="i am janhvi"
print("am" in a)
print("I" not in a)

#print characters using slice function
a="Janhvi Kudke"
print(a[2:9]) #nhvi Ku
print(a[5:])  # Kudke
print(a[:6])  #Janhvi

#negative indexing
print(a[-4:-1]) #udk
print(a[:-1]) #Janhvi Kudk
print(a[-2:-5]) #can't run showing empty line

#modify strings
a=" Janhvi "
b="Kudke"
print(a.upper()) #upper() method
print(a.lower()) #lower() method
print(a.strip()) #strip() method
print(a.replace('J','T')) #replace() method
print(a.split(' ')) #split() method
print(a+b) #concatenation 
print(20,a+b) 

#format() method
name="janhvi"
surname="kudke"
age=20
print("{}".format('cutie')) 
print("my name is {} {} and my age is {}".format(name,surname,age))
print("my name is {1} {2} and my age is {0}".format(age,name,surname))

#Escape characters
a = "Janhvi is a daughter of \"Vandana\"."
print("Escape",a)

b = "I\'am Janhvi."
print(b)

c = "This will insert one \\ (backslash)."
print(c)

d = "Hlo\nhow are u?"
print(d)

e = "Sakharam\rKudke"
print(e)

f = "hlo\tworld!"
print(f)

#This example erases one character (backspace):
g = "whor \bu?"
print(g)

#string method()
x="my NAME Is kudke janhvi"
print(x.capitalize())
#first letter capital

print(x.casefold())
#all small letter

print(x.center(5))

print(x.count('k'))
#how many letters present

print(x.encode())

print(x.endswith('j'))
#if value present or not end then it writtens true false 

print(x.expandtabs()) 

print(x.find('k'))
#it writtens the position of values

print(x.format())


print(x.index('j'))

print(x.isalnum())

print(x.isalpha())

print(x.isdecimal())

print(x.isdigit())

print(x.isidentifier())

print(x.islower())

print(x.isnumeric())

print(x.isprintable())

print(x.isspace())

print(x.istitle())

print(x.isupper())

print("*".join(x))

print(x.ljust(20))

print(x.lower())

print(x.lstrip())

print(x.maketrans("j","T"))

print(x.partition("janhvi"))

print(x.replace("janhvi","anand"))

print(x.rfind("kudke"))

print(x.rindex("kudke"))

print(x.rjust(10))

print(x.rpartition("kudke"))

print(x.rsplit(","))

print(x.rstrip())

print(x.split())

print(x.splitlines())

print(x.startswith("I"))

print(x.strip())

print(x.swapcase())

print(x.title())

y={65:80}
print(x.translate(y))

print(x.upper())

y="30"
print(y.zfill(10))