class NodeEdge:
    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head
        self.link_tail = None
        self.link_head = None
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"({self.tail}:{self.head}:{self.link_head}:{self.link_tail})"