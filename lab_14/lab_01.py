#20180269 천성규
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.items[-1]
    
    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
            pos += 1
    
    def __str__(self):
        return str(self.items)
    
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
    def __init__(self, root):
        self.root = root
        
    def traverse_inorder(self):
        ret = []
        
        def inorder_recursive(root):
            if root == None:
                return
            
            inorder_recursive(root.left_child) #L
            ret.append(root) #V
            inorder_recursive(root.right_child) #R
            
        inorder_recursive(self.root)
        return ret
    
    def traverse_inorder_iterative(self):
        ret = []
        root = self.root
        stack = Stack()
        
        while not stack.is_empty() or root != None:
            while root != None:
                stack.push(root)
                root = root.left_child
                
            node = stack.peek()
            stack.pop()
            ret.append(node)
            
            root = node.right_child
        
        return ret
    
    def traverse_preorder(self):
        ret = []
        
        def preorder_recursive(root):
            if root == None:
                return
            
            ret.append(root) #V
            preorder_recursive(root.left_child) #L
            preorder_recursive(root.right_child) #R
            
        preorder_recursive(self.root)
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
         
    def traverse_levelorder(self):
        ret = []
        
        def height(node):
            if node is None:
                return 0
            else:
                lheight = height(node.left_child)
                rheight = height(node.right_child)
                
                if lheight > rheight:
                    return lheight + 1
                else:
                    return rheight + 1
        
        def levelorder_recursive(root, level):
            if root == None:
                return
            if level == 1:
                ret.append(root)
            elif level > 1:
                levelorder_recursive(root.left_child, level-1)
                levelorder_recursive(root.right_child, level-1)            
        
        h = height(root)
        for i in range(1, h + 1):
            levelorder_recursive(root, i)
        return ret
    
    def traverse_levelorder_iterative(self):
        ret = []
        root = self.root
        if root == None:
            return

        queue = Queue()
        queue.enqueue(root)
        
        while not queue.is_empty():
            ret.append(queue.peek())
            node = queue.peek()
            queue.dequeue()
            
            if node.left_child != None:
                queue.enqueue(node.left_child)
                
            if node.right_child != None:
                queue.enqueue(node.right_child)
                
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
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    
    actions = tree.traverse_inorder()
    print("inorder", actions)
    
    actions = tree.traverse_preorder()
    print("preorder", actions)
    
    actions = tree.traverse_postorder()
    print("postorder", actions)
    
    actions = tree.traverse_inorder_iterative()
    print("inorder_iterative", actions)
    
    actions = tree.traverse_levelorder()
    print(actions)
    
    actions = tree.traverse_levelorder_iterative()
    print(actions)
    