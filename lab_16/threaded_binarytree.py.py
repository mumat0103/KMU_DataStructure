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

class TreeNodeThreaded:
    def __init__(self, elem=None):
        self.elem = elem
        self.left_child = self.right_child = None
        self.left_thread = self.right_thread = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"
    
class ThreadedBinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.head = TreeNodeThreaded()
        self.head.left_thread = True
        self.head.right_thread = False
        self.head.left_child = self.head
        self.head.right_child = self.head
        
        self.__build()
    
    def __build(self):
        """using inorder traversal"""
        if self.root == None:
            return
        
        self.head.left_thread = False
        self.head.left_child = self.root
        
        stack = Stack()
        pred = self.head
        root = self.root
        
        while not stack.is_empty() or root != None:
            while root != None:
                stack.push(root)
                root = root.left_child
                
            node = stack.peek()
            stack.pop()
            
            if node.left_child == None:
                node.left_thread = True
                node.left_child = pred
                
            if pred.right_child == None:
                pred.right_thread = True
                pred.right_child = node
                
            root = node.right_child
            pred = node
            
        pred.right_child = self.head
        pred.right_thread = True

    def find_successor(self, root):
        node = root.right_child
        if not root.right_thread:
            while node is not None and not node.left_thread:
                node = node.left_child

        return node
    
    def traverse_inorder(self):
        ret = []
        root = self.find_successor(self.head)
        
        while root is not None and root is not self.head:
            ret.append(root)
            root = self.find_successor(root)
        
        return ret

class BTreeBuilder:
    @staticmethod
    def build(sexpr):
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
                stack.push(TreeNodeThreaded(token))
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
        
        return root

if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    root_ = BTreeBuilder.build(sexpr)
    tree = ThreadedBinaryTree(root_)
    
    root = tree.root
    e = root.left_child.right_child
    print(f"{e.left_child} <{e}> {e.right_child}")
    
    f = root.right_child.left_child
    print(f"{f.left_child} <{f}> {f.right_child}")
    
    g = root.right_child.right_child
    print(f"{g.left_child} <{g}> {g.right_child}")
    
    h = root.left_child.left_child.left_child
    print(f"{h.left_child} <{h}> {h.right_child}")
    
    i = root.left_child.left_child.right_child
    print(f"{i.left_child} <{i}> {i.right_child}")
    
    print()
    actions = tree.traverse_inorder()
    print(actions)