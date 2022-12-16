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

class BSTree:
    def __init__(self, root):
        self.root = root
        
    def traverse_preorder(self):
        ret = []
        
        def preorder_recursive(root):
            if root == None:
                return
            
            ret.append(root)
            preorder_recursive(root.left_child)
            preorder_recursive(root.right_child)
            
        preorder_recursive(self.root)
        return ret
    
    def search(self, elem):
        if self.root is None:
            raise Exception("the root is none")
        
        def search_recursive(root):
            if root == None:
                return

            if elem == root.elem:
                return root
            
            root = (search_recursive(root.left_child)
                    if elem < root.elem 
                    else search_recursive(root.right_child)
                    )
            return root        
        return search_recursive(self.root)
    
    def search(self, elem):
         if self.root == None:
             raise Exception("the root is none")

         root = self.root
         while root is not None and elem != root.elem:
             root = root.left_child if elem < root.elem else root.right_child

         return root
        
    def insert(self, elem):
        parent = None
        root = self.root
        
        while root is not None and elem != root.elem:
            parent = root
            root = root.left_child if elem < root.elem else root.right_child
            
        if root is not None:
            return
        
        node_new = TreeNode(elem)
        if parent is None:
            self.root = node_new
            return
        
        if parent.elem > node_new.elem:
            parent.left_child = node_new
        else:
            parent.right_child = node_new
            
    def insert(self, elem):
        def insert_recursive(root):
            if root == None:
                return TreeNode(elem)
            
            if elem == root.elem:
                return root
            
            if elem < root.elem:
                root.left_child = insert_recursive(root.left_child)
            else:
                root.right_child = insert_recursive(root.right_child)
                
            return root
    
        self.root = insert_recursive(self.root)
            
    def delete(self, elem):
        def delete_recursive(root):
            nonlocal elem
            if root is None:
                return root

            if elem < root.elem:
                root.left_child = delete_recursive(root.left_child)
            elif elem > root.elem:
                root.right_child = delete_recursive(root.right_child)
            else:
                if root.left_child is None:
                    temp = root.right_child
                    root = None
                    return temp
                elif root.right_child is None:
                    temp = root.left_child
                    root = None
                    return temp

                current = root
                current = current.left_child
                
                while current.right_child is not None:
                    current = current.right_child
                    
                root.elem = current.elem
                
                elem = root.elem
                root.left_child = delete_recursive(root.left_child)

            return root
        
        self.root = delete_recursive(self.root)
    
if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    root = BTreeBuilder.build(sexpr)
    tree = BSTree(root)
    
    # found = tree.search(5)
    # print(found)
    # found = tree.search(2)
    # print(found)
    # found = tree.search(40)
    # print(found)
    # found = tree.search(30)
    # print(found)
    # found = tree.search(35)
    # print(found)

    tree.insert(80)
    actions = tree.traverse_preorder()
    print(actions)
    
    tree.delete(80)
    actions = tree.traverse_preorder()
    print(f"{actions}")