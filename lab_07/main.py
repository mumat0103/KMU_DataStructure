from stacks import Stack

N = 4
stack = Stack(N)

print("Length: ", len(stack))
print("Is Empty: ", stack.is_empty())
print("Push from 1 to", N)
for i in range(1, N+1):
    print("Push: ", i)
    stack.push(i)
    print("Stack: ", stack)
    print("Peek: ", stack.peek())