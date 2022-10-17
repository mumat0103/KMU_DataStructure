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
            node_new.rlink = node_new.llink = node_new
            self.head = node_new
        else:
            node_new.rlink = self.head
            node_new.llink = self.head.llink
            self.head.llink.rlink = node_new
            self.head.llink = node_new
            self.head = node_new

    def add_tail(self, node_new):
        if self.head is None:
            node_new.rlink = node_new.llink = node_new
            self.head = node_new
        elif self.head.rlink == self.head.llink == self.head:
            node_new.rlink = self.head
            node_new.llink = self.head
            self.head.rlink = node_new
            self.head.llink = node_new
        else:
            tmp = self.head
            while tmp.rlink is not self.head:
                tmp = tmp.rlink  # tmp = tail
            node_new.llink = tmp
            node_new.rlink = self.head
            tmp.rlink = node_new
            self.head.llink = node_new

    def delete_head(self):
        if self.head is None:
            raise Exception("List is Empty")
        elif self.head.llink == self.head.rlink == self.head:
            self.head = None
        else:
            tmp = self.head
            while tmp.rlink is not self.head:
                tmp = tmp.rlink  # tmp = tail
            tmp.rlink = self.head.rlink
            self.head.rlink.llink = tmp

    def delete_tail(self):
        if self.head is None:
            raise Exception("List is Empty")
        elif self.head.llink == self.head.rlink == self.head:
            self.head = None
        else:
            tmp = self.head
            while tmp.rlink is not self.head:
                tmp = tmp.rlink  # tmp = tail
            tmp.llink.rlink = self.head
            self.head.llink = tmp.llink

    def insert_before(self, node, node_new):
        if self.head.rlink is None and self.head.llink is None:
            self.add_head(node_new)
        else:
            tmp = self.head
            while tmp.rlink != node:
                tmp = tmp.rlink  # tmp = node 직전
            node_new.llink = tmp
            node_new.rlink = tmp
            tmp.rlink = node_new
            node.llink = node_new

    def insert_after(self, node, node_new):
        if self.head.rlink is None and self.head.llink is None:
            self.add_tail(node_new)
        else:
            tmp = self.head
            while tmp != node:  # tmp = node
                tmp = tmp.rlink
            if tmp.rlink is None:
                self.add_tail(node_new)
            else:
                node_new.llink = tmp
                node_new.rlink = tmp.rlink
                tmp.rlink.llink = node_new
                tmp.rlink = node_new

    def delete(self, node):
        if self.is_empty():
            raise Exception("List is Empty")
        else:
            tmp = self.head
            while tmp == node:  # tmp = node
                tmp = tmp.rlink
            if tmp == self.head:
                self.head = tmp.rlink
            tmp.llink.rlink = tmp.rlink
            tmp.rlink.llink = tmp.llink

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
        return self.head is None

    def __str__(self):
        if not self.is_empty():
            ret = []
            tmp = self.head
            tmp = tmp.rlink
            while tmp != self.head:
                ret.append(tmp)
                tmp = tmp.rlink
            return str(ret)
        else:
            return str([])


if __name__ == "__main__":
    list_ = CircularDoublyLinkedList()
    list_.add_tail(Node(10))
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
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
    print(list_)
    while not list_.is_empty():
        list_.delete_tail()
    print(list_)
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
    print(list_)
    list_.insert_after(Node(30), Node(40))
    print(list_)
    list_.insert_before(Node(20), Node(10))
    print(list_)
    print()
    list_.delete(Node(40))
    print(list_)
    list_.delete(Node(30))
    print(list_)
    list_.delete(Node(20))
    print(list_)
