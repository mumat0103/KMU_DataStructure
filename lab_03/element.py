class Element:
    def __init__(self, num=0):
        self.num = num
        
    def __str__(self):
        return f"Element: {self.num}"
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        if not isinstance(other, Element):
            raise Exception()
        
        add_ = self.num + other.num
        return Element(add_)
    
    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception()
        
        sub_ = self.num - other.num
        return Element(sub_)