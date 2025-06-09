# try...except
try:
    print(x)
    print("hello",x)
except:
    print("invalid")

#  try...except...except
try:
    print(y)
except NameError:
    print("\nvariable not define")
except:
    print("something is wrong")

# try...except...else
try:
    print("\njanhvi")
except:
    print("something is wrong")
else:
    print("program is run")

# try...except...finally
try:
    print("\njanhvi")
except:
    print("invalid")
finally:
    print("both block are finished")

# raise exception
x=-7
if x < 0:
    raise Exception("no nums below zero")

# raise typeerror
x="janhvi"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

    