import re

x="hlo,my name is janhvi"
print(re.search("^hlo.*hii$",x))
print(re.findall("hl",x))
print(re.split("\s",x,1))
print(re.sub("a","11",x))

y="i'm 11 Metacharacters"
print(re.search("[a-t]",y))
print(re.findall("\d",y))