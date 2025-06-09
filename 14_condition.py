a=int(input("enter the a: "))
b=int(input("enter the b: "))
m=int(input("enter your marks: "))
# if
if a>b:
    print("a is greater than b")
if a>b:print ("a is greater")
print()

# if else
if a>b:
    print("a is greater than b")
else :
    print("b is greater than a")
print()
print(a,"a is greater")if a>b else print (b,"b is greater")
print()
print(a,"a is greater")if a>b else print("both are same")if a==b else print(b,"b is greater")
print()

# if elif else
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("both a and b are same")
print()

#using add
if a>10 and b>10:
    print("both conditions are true")

#using or
if a>10 or b>10:
    print("at least one condition is true")

#using not
if not a!=b:
    print("both are same") 

#nested if
if m>35:
    print("you are pass")
    if m>75:
        print("you got first class,congrats!!!")
else:
    print("you are fail,better luck next time")

