SIZE = 20

arr = [i for i in range(1, SIZE+1)]

# print()
# print("addr   \tvalue")
# for i in range(SIZE):
#     print(id(arr[i]) ,arr[i])
    
#------------------------------------------------------------

class Person:
    def __init__(self, name="", age=0, salary=0.0):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f"{self.name}, {self.age}, {self.salary}"
    
james = Person("James", 20, 100.0)
edward = Person("Edward", 21)

# print(james)
# print(edward)

#------------------------------------------------------------

# v = None
# if not v:
#     print("Here1")
    
# if v is None:
#     print("Here2")
    
# v = 0
# if not v:
#     print("Here3")
    
# if v is None:
#     print("Here4")
    
# str_ = ""
# if not str_:
#     print("Here5")
    
# if str_ is None:
#     print("Here6")
    
#------------------------------------------------------------
class Item:
    def __init__(self, data):
        self.data = data
        self.link = None
        
    def __str__(self):
        return f"Item: {self.data}"
    
def explore(i):
    while i is not None:
        print(f"({i})", end="->")
        i = i.link
    print("\b\b")
        
item0 = Item(0)
item1 = Item(1)
item2 = Item(2)

item0.link = item1
item1.link = item2
explore(item0)