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
    
class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        
    def add_head(self, node_new):
        if self.tail == None:
            self.tail = node_new
        else:
            tail = self.tail
            while self.tail.llink != None: #Head 찾기
                self.tail = self.tail.llink
            
            self.tail.llink = node_new #Head의 llink를 새 노드로
            node_new.rlink = self.tail #새 노드의 rlink를 찾은 Head로
            self.tail = tail #self.tail 복구
    
    def add_tail(self, node_new):
        if self.tail == None:
            self.tail = node_new
        else:
            self.tail.rlink = node_new
            node_new.llink = self.tail
            self.tail = node_new
        
    def delete_head(self):
        if self.tail == None:
            raise Exception("self.tail is None")
        
        temp = self.tail        
        while True:
            if temp.llink == None: #Head 찾기
                break
            temp = temp.llink
            
        if temp.rlink == None:
            self.tail = None
            return
        
        temp.rlink.llink = None
        temp = None
        
    def delete_tail(self):
        if self.tail == None:
            raise Exception("self.tail is None")
       
        self.tail = self.tail.llink
    
    def insert_before(self, node, node_new): #node 앞에 삽입
        temp = self.tail
        
        if str(self.tail) == str(node): #node가 tail인 경우
            if self.tail.llink != None:
                node_new.llink = self.tail.llink
                node_new.rlink = self.tail
                self.tail.llink.rlink = node_new
                self.tail.llink = node_new
                return
            else:
                self.add_head(node_new)
                return
        
        while True: #node 찾기
            if str(temp) == str(node):
                break
            temp = temp.llink
        if temp.llink == None:
            self.add_head(node_new)
        else:
            node_new.rlink = temp
            node_new.llink = temp.llink
            temp.llink.rlink = node_new
            temp.llink = node_new
    
    def insert_after(self, node, node_new): #node 뒤에 삽입
        temp = self.tail

        if str(self.tail) == str(node): #tail 뒤에 넣는 경우
            self.add_tail(node_new)
            return
        
        while True: #node 찾기
            if str(temp) == str(node):
                break
            temp = temp.llink
        
        if temp.llink == None: #head 뒤에 넣는 경우
            temp.rlink.llink = node_new
            node_new.rlink = temp.rlink
            node_new.llink = temp
            temp.rlink = node_new
            return
        
        node_new.rlink = temp.rlink.llink
        temp.rlink.llink = node_new
        node_new.llink = temp
        temp.rlink = node_new
        
    
    def delete(self, node):
        temp = self.tail
        while True: #node 찾기
            if str(temp) == str(node):
                break
            temp = temp.llink
            
        temp.llink.rlink = temp.rlink
        temp.rlink.llink = temp.llink
        temp = None
    
    def __str__(self):
        result = []
        
        temp = self.tail
        while temp != None:
            result.append(temp.item)
            temp = temp.llink

        return f"{result[::-1]}"
    
if __name__ == "__main__":
    list_ = DoublyLinkedList()
    list_.add_head(Node(50))
    list_.add_tail(Node(100))
    list_.add_tail(Node(150))
    print("1", list_)
    
    list_.delete_head()
    print("2", list_)
    list_.delete_tail()
    print("3", list_)
    list_.delete_tail()
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
    print("8", list_)

    list_.insert_before(Node(50), Node(750))
    print("9", list_)

    list_.insert_after(Node(50), Node(123))
    print("10 insert_after(Node(50), Node(123)\n", list_)

    list_.insert_before(Node(50), Node(456))
    print("11 insert_before(Node(50), Node(456)\n", list_)
    
    list_.delete(Node(250))
    print("12 delete Node(250)\n", list_)
    
    list_.insert_before(Node(700), Node(567))
    print("13 insert_before(Node(700), Node(567)\n", list_)
    
    list_.insert_after(Node(700), Node(678))
    print("13 insert_after(Node(700), Node(678)\n", list_)
    
    list_.add_head(Node(777))
    list_.insert_after(Node(777), Node(888))
    print("13 insert_after(Node(777), Node(888)\n", list_)