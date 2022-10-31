class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap
        
    def __setitem__(self, id, elem):
        self.elems[id] = elem
        
    def __getitem__(self, id):
        return self.elems[id]

    def __str__(self):
        return f"{self.elems}"