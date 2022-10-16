from arrays import Array

class Queue:
    CAPACITY = 10
    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.front = self.rear = -1
        
    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity
            
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def enqueue(self, elem):
        if self.is_full():
            raise Exception("stack is full.")

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = elem
        
        if self.front < 0:
            self.front = 0
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        
        self.arr[self.front] = None
        
        if self.front == self.rear:
            self.front = self.rear = -1
            return
        
        self.front = (self.front + 1) % self.capacity
        print(self.front)
    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        
        return self.arr[self.front]
        
    def __len__(self):
        if self.is_empty():
            return 0
        
        if self.rear < self.front:
            return self.capacity - self.front + self.rear + 1
        return self.rear - self.front + 1
    
    def __iter__(self):
        if self.is_empty():
            return
            
        pos = self.front
        for i in range(pos, pos + len(self)):
            yield self.arr[i % self.capacity]
            
    def __str__(self):
        return str(self.arr)
    
if __name__ == "__main__":
    N = 8
    queue = Queue(N)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    print(queue)
    print("Peek: ", queue.peek()) #A
    queue.dequeue() #idx = 1
    print("Peek: ", queue.peek()) #B
    queue.dequeue() #idx = 2
    print(queue)
    queue.enqueue("E")
    queue.enqueue("F")
    queue.enqueue("G")
    queue.enqueue("H")
    queue.enqueue("I")
    queue.enqueue("J")
    print(queue)
    queue.dequeue() #idx = 3
    print(queue)
    
    for i in queue: #front = 3, rear = 1
        print("Element: ", i)
    print("Peek: ", queue.peek())
    
    while not queue.is_empty():
        queue.dequeue()
    print(queue)