from element import Element
from elements import Elements

elems = Elements()
elems[0] = Element(20)
elems[1] = Element(20)

print(elems)

size = 10
list_ = [0] * size
print(list_)

list_ = [Element(10) for _ in range(size)]
print(list_)

list_[0].num = 99
print(list_)