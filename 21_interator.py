name=("yogi","dnyano","anju")
frd=iter(name)

print(next(frd))
print(next(frd))
print(next(frd))

class Table:
    def __iter__(self):
        self.x=2
        return self
    def __next__(self):
        y=self.x
        self.x+=2
        return y
        
a=Table()
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

class Table:
    def __iter__(self):
        self.x=2
        return self
    def __next__(self):
        if self.x<=8:
            y=self.x
            self.x+=2
            return y
        else:
            raise StopIteration
a=Table()
b=iter(a)
for i in b:
    print(i)