from arrays import Array

class Queue:
    CAPACITY = 10
    
    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.front = self.rear = -1
        
    def is_full(self):
        return self.rear >= self.capacity - 1
    
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def enqueue(self, elem):
        if self.is_full():
            raise Exception("stack is full.")

        self.rear += 1
        self.arr[self.rear] = elem
        
        if self.front < 0:
            self.front = 0
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        
        self.arr[self.front] = None
        
        if self.front == self.rear and self.front != -1:
            self.front = self.rear = -1
        else:
            self.front += 1
        
    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        
        return self.arr[self.front]
        
    def __len__(self):
        return 0 if self.is_empty() else self.rear - self.front + 1
    
    def __iter__(self):
        if self.is_empty():
            return
        
        pos = self.front
        while pos <= self.rear:
            yield self.arr[pos]
            pos += 1
            
    def __str__(self):
        return str(self.arr)
    
if __name__ == "__main__":
    N = 5
    q = Queue(N)
    print("Length:", len(q))
    print("Empty:", q.is_empty())
    print("Enqueue 1-", N)

    for i in range(1, N + 1):
        q.enqueue(i)
        print("Peeking:", q.peek())
        print("Queue =", q)
        
    print("Length:",len(q))
    print("Empty:", q.is_empty())
    
    while not q.is_empty():
        print("Peeking:", q.peek())
        q.dequeue()
        print("Queue =", q)
        
    print("Length:", len(q))
    print("Empty:", q.is_empty())