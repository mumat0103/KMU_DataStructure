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
            node_new.rlink = node_new.llink = self.head
        else:
            node_new.llink = self.head.llink
            node_new.rlink = self.head
            self.head.llink.rlink = node_new
            self.head.llink = node_new
            
            self.head = node_new

    def add_tail(self, node_new):
        if self.head is None:
            self.head = node_new
            node_new.rlink = node_new.llink = self.head
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

        node_new.rlink = temp.rlink
        node_new.llink = temp
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

        if temp is self.head:
            self.head = temp.rlink

        temp.rlink.llink = temp.llink
        temp.llink.rlink = temp.rlink

    def __iter__(self):
        self.current = self.head.llink
        self.count = 0
        return self

    def __next__(self):
        self.current = self.current.rlink
        if self.current is self.head and self.count == 1:
            raise StopIteration
        if self.current is self.head and self.count == 0:
            self.count += 1

        return self.current

    def is_empty(self):
        return True if self.head == None else False
    
    def __str__(self):
        result = []
        if not self.is_empty():
            temp = self.head
            result.append(temp.item)
            temp = temp.rlink
            while temp != self.head:
                result.append(temp.item)
                temp = temp.rlink                
            return f"{result}"
        else:
            return f"{result}"
    
if __name__ == "__main__":
    list_ = CircularDoublyLinkedList()
    list_.add_head(Node(10))
    list_.add_tail(Node(20))
    list_.add_tail(Node(30))
    print(list_)
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
    list_.delete_tail()
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