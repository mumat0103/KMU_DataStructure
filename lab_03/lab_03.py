class Barebone:
    pass

bb_01 = Barebone()
bb_02 = Barebone()
print(id(bb_01))
print(id(bb_02))
bb_03 = bb_01
print(bb_01 is bb_02)
print(bb_01 is bb_03, "\n")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name is : {self.name}, {self.age}"
        
st = Student("홍길동", 20)
print("__str__ )", st, "\n")

class Element:
    def __init__(self, num=0):
        self.num = num
        
    def __str__(self):
        return f"Element: {self.num}"
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        if not isinstance(other, Element):
            raise Exception()
        
        add_ = self.num + other.num
        return Element(add_)
    
    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception()
        
        sub_ = self.num - other.num
        return Element(sub_)
    
elem = Element()
print("__str__) ", elem, "\n")
elem = Element(10)
print(elem)

elems = [Element(100), Element(200)]
print(elems)

res = Element(10) + Element(10)
print(res)

res = Element(20) - Element(10)
print(res)

class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap
        
    def __setitem__(self, id, elem):
        self.elems[id] = elem
        
    def __getitem__(self, id):
        return self.elems[id]

    def __str__(self):
        return f"{self.elems}"

elems = Elements()
elems[0] = Element(10)
elems[1] = Element(20)

print("__setitem__", elems.elems[0])
print(elems.elems[1], "\n" )

print(elems[0])
print(elems[1])

print(elems)