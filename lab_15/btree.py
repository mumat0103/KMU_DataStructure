import copy
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
        
    def search_dfs(self, elem):
        ret = None
        
        def dfs_recursive(root): #preorder
            nonlocal ret
            if root == None:
                return
            
            if elem == root.elem:
                ret = root
                return
            dfs_recursive(root.left_child)
            dfs_recursive(root.right_child)
        
        def dfs_recursive_post(root): #postorder
            nonlocal ret
            if root == None:
                return
            
            dfs_recursive_post(root.left_child)
            dfs_recursive_post(root.right_child)
            if elem == root.elem:
                ret = root
                return
            
        def dfs_recursive_in(root): #inorder
            nonlocal ret
            if root == None:
                return
            
            dfs_recursive_in(root.left_child)
            if elem == root.elem:
                ret = root
                return
            dfs_recursive_in(root.right_child)
            
        dfs_recursive(self.root)
        return ret
    
    def search_bfs(self, elem):
        if self.root == None:
            return None
        
        root = self.root
        queue = Queue()
        queue.enqueue(root)
        ret = None
        
        while not queue.is_empty() and queue.peek().elem != elem:
            node = queue.peek()
            queue.dequeue()
            
            if node.left_child != None:
                queue.enqueue(node.left_child)
                
            if node.right_child != None:
                queue.enqueue(node.right_child)
        
        ret = None if queue.is_empty() else queue.peek()
        return ret
        
    def copy(self):  #iterative로 해보기
        def copy_recursive(root):
            if root == None:
                return
            
            node = TreeNode(root.elem)
            node.left_child = copy_recursive(root.left_child)
            node.right_child = copy_recursive(root.right_child)
            return node
        
        return BTree(copy_recursive(self.root))
    
    def copy_builtin(self):
        return copy.deepcopy(self)
    
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
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    for e in sexpr:
        found = tree.search_dfs(e)
        # print("target:", e, " found:", found)
        
    for e in sexpr:
        found = tree.search_bfs(e)
        print("target:", e, " found:", found)
        
    tree1 = tree.copy() #별도의 메모리
    tree2 = tree.copy_builtin() #별도의 메모리
    tree3 = tree #같은 메모리
    # print(id(tree1), id(tree2), id(tree), id(tree3))
    
    tree.root.left_child.right_child.elem = "Z"
    actions = tree.traverse_postorder()
    print(actions)
    actions = tree1.traverse_postorder()
    print(actions)
    tree1.root.left_child.right_child.elem = "W"
    actions = tree1.traverse_postorder()
    print(actions)
    actions = tree2.traverse_postorder()
    print(actions)
    actions = tree3.traverse_postorder()
    print(actions)

