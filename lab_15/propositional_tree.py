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
        self.value = None  # boolean value
        self.left_child = self.right_child = None
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.elem}"

class PropositionalTree:
    def __init__(self, root):
        self.root = root
    
    def calculate_propositional(self, *param):
        ret = None
        
        def calculate_recursive(root):
            nonlocal ret
            if root == None:
                return
            
            calculate_recursive(root.left_child)
            calculate_recursive(root.right_child)
            ret.append(root)
        
        calculate_recursive(self.root)
        return ret
    
    def traverse_postorder(self):
        ret = []
        
        def postorder_recursive(root):
            if root == None:
                return
            
            postorder_recursive(root.left_child)
            postorder_recursive(root.right_child)
            ret.append(root)
            
        postorder_recursive(self.root)
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
        
        return root
    
if __name__ == "__main__":
    sexpr = "( OR ( OR ( AND ( 0 NOT ( # 1 ) ) AND ( NOT ( # 0 ) 2 ) ) NOT ( # 2 ) ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = PropositionalTree(root)
    actions = tree.traverse_postorder()
    print(actions)
    # prop = tree.calculate_propositional(False, True, False)
    # print(prop.value)
    
    #x0 = 0 x1 = 1 x2 = 2