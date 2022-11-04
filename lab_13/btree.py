#20180269 천성규

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return not self.items
    
    def push(self, elem):
        self.items.append(elem)
        
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        self.items.pop()
        
    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        return self.items[-1]

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
        pos += 1
        
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_child = None
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.elem}"
    
class BTree:
    def __init__(self):
        self.root = None
        
    def build(self, sexpr):
        stack = Stack()
        s_stack = Stack()
        it = iter(sexpr)
        root = None
        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break
            
            if token != ")":
                stack.push(TreeNode(token))
                continue
            
            prev = None
            while stack.peek().elem != "(":
                node = stack.peek()
                stack.pop()
                prev = node
                s_stack.push(prev)
            
            stack.pop()
            
            if stack.is_empty():
                root = prev
                continue
            
            root = stack.peek()
            if not s_stack.is_empty():
                if s_stack.peek().elem != "#":
                    root.left_child = s_stack.peek()
                    s_stack.pop()
                else:
                    s_stack.pop()
                
                if s_stack.peek().elem != "#":
                    root.right_child = s_stack.peek()
                    s_stack.pop()
                else:
                    s_stack.pop()
                    
            stack.pop()
            stack.push(root)
            
        if not stack.is_empty():
            raise Exception("expression is wrong.")
        
        self.root = root
        

if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )".split()
    tree = BTree ()
    tree.build(sexpr)
    root = tree.root
    print(root)
    print(root.left_child)
    print(root.left_child.left_child)
    print(root.left_child.right_child)
    print(root.right_child)
    print(root.right_child.left_child)
    print(root.right_child.right_child)
    print()
    
    sexpr = "( 30 )".split()
    tree = BTree()
    tree.build(sexpr)
    root = tree.root
    print(root)
    print(root.left_child)
    print(root.right_child)
    print()
    
    sexpr = "( 30 ( 5 10 ) )".split()
    tree = BTree()
    tree.build(sexpr)
    root = tree.root
    print(root)
    print(root.left_child)
    print(root.right_child)
    
#full Btree = 0개 or 2개
#complete Btree = 왼쪽부터 채우는가