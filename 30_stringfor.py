a=10.98
msg="price is {} rupees"
msg1="price is {:.3f} rupees"
print(msg.format(a))
print("\n",msg1.format(a))

# multiple values
qua=10
itemno=3
price=52.589
msg="I want {} pieces of item number {} for {:.2f} rupees"
print("\n",msg.format(qua,itemno,price))

# index number
qua=10
itemno=3
price=52.589
msg="I want {2} pieces of item number {0} for {1:.2f} rupees"
print("\n",msg.format(itemno,price,qua))

age=20
name="janhvi"
msg="my name is {0} you know {0} means Ganga and i'm {1} years old"
print("\n",msg.format(name,age))

# named indexes
x="my name is {name}, and i'm {year} years old"
print("\n",x.format(name="janhvi",year=20))