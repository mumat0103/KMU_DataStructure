#20180269 천성규

from circular_doubly_linked_list import *

class Queue:
    def __init__(self):
        self.list_ = CircularDoublyLinkedList()
    
    def enqueue(self, elem):
        self.list_.add_tail(Node(elem))
        
    def dequeue(self):
        self.list_.delete_head()
        
    def peek(self):
        return self.list_.head
        
    def is_empty(self):
        return self.list_.is_empty()    
        
    def __iter__(self):
        return iter(self.list_)
            
    def __str__(self):
        return str(self.list_)
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue)
    
    print("peek:", queue.peek())
    queue.dequeue()
    print(queue)
    
    queue.enqueue(30)
    print(queue)
    queue.enqueue(40)
    print(queue)
    print("peek:", queue.peek())
    queue.dequeue()
    print(queue)
    
    for i in queue:
        print("Element:", i)
    