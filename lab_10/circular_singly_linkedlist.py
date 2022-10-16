class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False
    
    def __str__(self):
        return f"{self.item}"
    
class circularSinglyLinkedList:
    def __init__(self):
        self.tail = None
        
    def add_head(self, node_new):
        if self.tail is None:
            self.tail = node_new
            node_new.next = node_new
        else:
            node_new.next = self.tail.next #무조건 HEAD임
            self.tail.next = node_new

    def add_tail(self, node_new):
        if self.tail is None:
            self.tail = node_new
            node_new.next = node_new
        else:
            node_new.next = self.tail.next #node_new.next를 HEAD로
            self.tail.next = node_new
            self.tail = node_new
            
    def delete_head(self):
        if self.tail == None:
            raise Exception("Cannot Delete Head")
        
        if  self.tail == self.tail.next:
            self.tail = None
        else:
            temp = self.tail.next #무조건 HEAD임
            self.tail.next = temp.next
    
    def delete_tail(self):
        if self.tail == None:
            raise Exception("Cannot Delete Tail")
        
        if self.tail == self.tail.next:
            self.tail = None
        else:
            temp = self.tail
            while temp.next != self.tail: #tail 앞 node 찾기
                temp = temp.next
                
            temp.next = self.tail.next
            self.tail = temp
            
    def insert_after(self, node, node_new): #뒤에
        temp = self.tail

        while str(temp.next) != str(node): #node 찾기
            temp = temp.next

        if temp.next == self.tail:
            node_new.next = self.tail.next
            self.tail.next = node_new
            self.tail = node_new
        else:
            node_new.next = temp.next.next
            temp.next.next = node_new

        
    def insert_before(self, node, node_new): #앞에
        temp = self.tail

        while str(temp.next) != str(node):
            temp = temp.next
        node_new.next = temp.next
        temp.next = node_new
            
    def delete(self, node):
        temp = self.tail
        
        if temp is not None:
            if temp.item == node.item:
                self.tail = temp.next
                temp = None
                return
            
        while temp is not None:
            if temp.item == node.item:
                break
            prev = temp
            temp = temp.next
            
        if temp is None:
            return
        
        prev.next = temp.next
        temp = None
    
    def __str__(self):
        result = []

        if self.tail is not None:
            iterator = self.tail.next

            if iterator is not None:
                result.append(iterator.item)
                iterator = iterator.next

            while iterator is not self.tail.next:
                result.append(iterator.item)
                iterator = iterator.next

        return f"{result}"
    
if __name__ == "__main__":
    list_ = circularSinglyLinkedList()
    list_.add_head(Node(50))
    list_.add_tail(Node(100))
    list_.add_tail(Node(150))
    print("1", list_)

    list_.delete_head()
    print("2", list_)
    list_.delete_tail()
    print("3", list_)
    list_.delete_head()
    print("4", list_)

    list_.add_tail(Node(150))
    list_.insert_before(Node(150), Node(999))
    print("5", list_)

    list_.add_head(Node(50))
    list_.add_tail(Node(100))
    print("6", list_)

    list_.add_tail(Node(700))
    print("7", list_)

    list_.insert_after(Node(50), Node(250))
    list_.insert_after(Node(700), Node(250))
    print("8", list_)

    list_.insert_before(Node(50), Node(750))
    print("9", list_)

    list_.delete(Node(250))
    print("10 delete Node(250)", list_)