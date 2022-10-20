class Node:
    def __init__(self, coef, exp):
        self.coef = coef #계수
        self.exp = exp #차수
        self.next = None
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False

    def __str__(self):
        return f"({self.coef})x^{self.exp} + "
    
class SinglyLinkedList:
    def __init__(self):
        self.head = self.next_ = None
        
    def __iter__(self):
        self.next_ = self.head
        return self
    
    def __next__(self):
        if self.next_ is not None:
            temp = self.next_
            self.next_ = self.next_.next
            return temp
        else:
            raise StopIteration
               
    def add_head(self, node_new):
        self.next_ = node_new
        
        if self.head is None:
            self.head = node_new
        else:
            temp = self.head
            self.head = node_new
            self.head.next = temp
    
    def add_tail(self, node_new):
        if self.head is None:
            self.head = node_new
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            
            tail.next = node_new
    
    def delete_tail(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                temp.next = None

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
            
    def insert_after(self, node, node_new):
        temp = self.head
        while temp != node:
            temp = temp.next
        if temp.next == None:
            self.add_tail(node_new)
            return
        node_new.next = temp.next
        temp.next = node_new
                
    def insert_before(self, node, node_new):
        if self.head == node:
            self.add_head(node_new)
        else:
            temp = self.head

            while temp.next != node:
                temp = temp.next
            
            node_new.next = temp.next
            temp.next = node_new
    
    def delete(self, node):
        temp = self.head
        
        if temp is not None:
            if temp.item == node.item:
                self.head = temp.next
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
        res = []
        iterator = self.head
        
        while iterator != None:
            res.append(str(iterator))
            iterator = iterator.next
        
        str_ = "".join(res)
        return f"{str_}\b\b"
    
class Polynomial():
    def __init__(self):
        self.expr = SinglyLinkedList()

    def get_lead_exp(self):
        return self.expr.head.exp
    
    def evaluate(self, x):
        list_ = []
        list_.append(self.expr.head)
        
        temp = self.expr.head
        while temp.next != None:
            temp = temp.next
            list_.append(temp)
        
        return sum(i.coef * x ** i.exp for i in list_)
    
    def find_term(self, exp):
        temp = self.expr.head
        while True:
            if temp == None:
                break
            
            if temp.exp == exp:
                return temp
            
            temp = temp.next
    
    def attach(self, coef, exp):
        if self.expr == None:
            self.expr.add_head(Node(coef, exp))
        else:
            self.expr.add_tail(Node(coef, exp))
        return self
    
    def __str__(self):
        return str(self.expr)
    
    def __add__(self, other):
        poly = Polynomial()
        term_a = self.expr.head
        term_b = other.expr.head
        
        while term_a != None and term_b != None:
            if term_a.exp > term_b.exp:
                poly.attach(term_a.coef, term_a.exp)
                term_a = term_a.next
            elif term_a.exp < term_b.exp:
                poly.attach(term_b.coef, term_b.exp)
                term_b = term_b.next
            else:
                coef = term_a.coef + term_b.coef
                if coef != 0:
                    poly.attach(coef, term_a.exp)
                term_a = term_a.next
                term_b = term_b.next
        
        return poly
    
    def __mul__(self, other):
        poly = Polynomial()
        
        for i in self.expr:
            for j in other.expr:
                exp = i.exp + j.exp
                coef = i.coef * j.coef
                
                term = poly.find_term(exp)
                if term == None:
                    poly.attach(coef, exp)
                else:
                    term.coef += coef
                    
        return poly
if __name__ == "__main__":
    poly = Polynomial()
    poly.attach(3, 20).attach(2, 5).attach(4, 0)
    print(poly)

    x = 3
    res = poly.evaluate(x)
    print(f"{poly} = {res}, where x = {x}")

    print("get_lead_exp = ", poly.get_lead_exp())
    print("get_coef(20) = ", poly.find_term(20))
    
    
    poly1 = Polynomial()
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)
    
    poly2 = Polynomial()
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)
    
    print()
    poly = poly1 + poly2
    print("poly =\n", poly)
    print()
    
    poly3 = Polynomial()
    poly3.attach(1,1).attach(1,0)
    print("poly3 = \n", poly3)
    
    poly4 = Polynomial()
    poly4.attach(1,2).attach(-5,1).attach(-6,0)
    print("poly4 = \n", poly4)
    
    print()
    poly = poly3 * poly4
    print("poly =\n", poly)