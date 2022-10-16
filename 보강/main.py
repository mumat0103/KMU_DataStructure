def foo():
    print("Hello World")
    
f = foo()
print(type(f))

def gen(n):
    for i in range(n):
        yield i
        
g = gen(10)
print(type(g))

print(next(g))
print(next(g))
print(next(g))
