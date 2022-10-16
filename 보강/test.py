from collections.abc import Iterable

class OddGen:
    def __init__(self, bgn ,end):
        self.bgn = bgn
        self.end = end
        self.odd = self.bgn
        
    # def __iter__(self):
    #     for i in range(self.bgn, self.end):
    #         if i % 2:
    #             yield i
    
    def __next__(self):
        if self.odd >= self.end:
            self.odd = self.bgn
            raise StopIteration
        
        odd = self.odd
        self.odd += 1
        if odd % 2:
            return odd
        
        return next(self)
    
    def __iter__(self):
        self.odd = self.bgn
        return self
    
odd_gen = OddGen (10, 30)
print(type(odd_gen))
print(isinstance(odd_gen , Iterable)) # False
for i in odd_gen:
    print("Odd number:", i)

it = iter(odd_gen)
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))



# list_ = [1, 2, 3]
# print(type(list_), isinstance(list_, Iterable))
# tuple_ = (1, 2, 3)
# print(type(tuple_), isinstance(tuple_, Iterable))
# dict_ = {1: "Hello", 2: "World"}
# print(type(dict_), isinstance(tuple_, Iterable))
# set_ = {1, 2, 3}
# print(type(set_), isinstance(set_, Iterable))
# str_ = "Hello World"
# print(type(str_), isinstance(str_, Iterable))
# int_ = 10
# print(type(int_), isinstance(int_, Iterable))

# class Foo:
#     pass

# foo = Foo()
# print(type(foo), isinstance(foo, Iterable))