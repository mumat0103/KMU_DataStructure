#20180269 천성규
class Node:
    def __init__(self, item=None):
        self.item = item
        self.llink = self.rlink = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True
        return False

    def __str__(self):
        return f"{self.item}"

    def __repr__(self):
        return str(self)

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, node_new):
        if self.head is None:
            self.head = node_new
            node_new.rlink = node_new.llink = node_new
        else:
            node_new.llink = self.head.llink
            node_new.rlink = self.head
            self.head.llink.rlink = node_new
            self.head.llink = node_new
            
            self.head = node_new

    def add_tail(self, node_new):
        if self.head is None:
            self.head = node_new
            node_new.rlink = node_new.llink = node_new
        else:
            node_new.llink = self.head.llink
            node_new.rlink = self.head
            self.head.llink.rlink = node_new
            self.head.llink = node_new

    def delete_head(self):
        if self.is_empty():
            raise Exception("list is empty.")
        if self.head == self.head.llink == self.head.rlink:
            self.head = None
        else:
            self.head.llink.rlink = self.head.rlink
            self.head.rlink.llink = self.head.llink
            self.head = self.head.rlink

    def delete_tail(self):
        if self.is_empty():
            raise Exception("list is empty.")
        
        if self.head == self.head.llink == self.head.rlink:
            self.head = None
        else:
            tail = self.head.llink
            tail.llink.rlink = self.head
            self.head.llink = tail.llink

    def insert_after(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        
        temp = self.head

        while str(temp) != str(node):
            temp = temp.rlink

        node_new.llink = temp
        node_new.rlink = temp.rlink
        temp.rlink.llink = node_new
        temp.rlink = node_new


    def insert_before(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        
        temp = self.head

        while str(temp) != str(node):
            temp = temp.rlink

        if temp is self.head:
            self.add_head(node_new)
        else:
            node_new.rlink = temp
            node_new.llink = temp.llink
            temp.llink.rlink = node_new
            temp.llink = node_new

    def delete(self, node):
        if self.is_empty():
            raise Exception("list is empty.")
        
        temp = self.head

        while str(temp) != str(node):
            temp = temp.rlink

        if temp == self.head:
            self.delete_head()
            return
        if temp == self.head.llink:
            self.delete_tail()
            return
        prev = temp.llink
        next = temp.rlink
        prev.rlink = next
        next.llink = prev

    def __iter__(self):
        self.next_ = None
        return self

    def __next__(self):
        if self.head == None or self.next_ == self.head:
            raise StopIteration
        
        res = self.head if self.next_ == None else self.next_
        self.next_ = res.rlink
        return res

    def is_empty(self):
        return True if self.head == None else False
    
    def __str__(self):
        result = []
        for i in self:
            result.append(i)
        
        return str(result)

class Stack:
    def __init__(self):
        self.list_ = CircularDoublyLinkedList()
        
    def push(self, elem):
        self.list_.add_head(Node(elem))
    
    def pop(self):
        if self.is_empty():
            raise Exception("list is empty.")
        
        self.list_.delete_head()
    
    def peek(self):
        if self.is_empty():
            raise Exception("list is empty.")
        
        return self.list_.head
    
    def is_empty(self):
        return self.list_.is_empty()
            
    def __iter__(self):
        return iter(self.list_)
    
    def __str__(self):
        return str(self.list_)
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack)
    
    print("Peek:", stack.peek())
    stack.pop()
    print(stack)
    stack.push(30)
    print(stack)
    stack.push(40)
    print(stack)
    print("Peek:", stack.peek())
    stack.pop()
    print(stack)
    
    for i in stack:
        print("Element:", i)
        
    print()
    print(stack)
    while not stack.is_empty():
        print("peek:", stack.peek())
        stack.pop()
        print(stack)