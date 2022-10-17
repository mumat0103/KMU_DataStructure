#20180269 천성규
class Node:
    def __init__(self, item=None):
        self.item = item
        self.rlink = self.llink = None
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False
    
    def __str__(self):
        return f"{self.item}"
    
    def __repr__(self):
        return set(self)
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_head(self, node_new):
        if self.is_empty():
            node_new.llink = node_new
            node_new.rlink = node_new
            self.head = node_new
        else:
            pass
            
    def add_tail(self, node_new):
        raise NotImplemented
        
    def delete_head(self):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented
        
    def delete_tail(self):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented
    def insert_before(self, node, node_new): #node 앞에 삽입
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented
    def insert_after(self, node, node_new): #node 뒤에 삽입
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented
    
    def delete(self, node):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented
    
    def __iter__(self):
        raise NotImplemented
    
    def __next__(self):
        raise NotImplemented
    
    def is_empty(self):
        return True if self.head == None else False
    
    def __str__(self):
        raise NotImplemented
if __name__ == "__main__":
    list_ = CircularDoublyLinkedList()
    list_.add_head(Node(10))
    list_.add_tail(Node(20))
    list_.add_tail(Node(30))
    print("1", list_)
    for i in list_:
        print("Element:", i)
    print()
    it = iter(list_)
    while True:
        try:
            i = next(it)
        except StopIteration:
            break
        print("Element:", i)
        
    print(list_)
    while not list_.is_empty():
        list_.delete_tail()
        print(list_)
        
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
    print(list_)
    
    list_.insert_after(Node(30), Node(40))
    list_.insert_before(Node(20), Node(10))
    print(list_)

    list_.delete(Node(40))
    print(list_)
    list_.delete(Node(30))
    print(list_)
    list_.delete(Node(20))
    print(list_)