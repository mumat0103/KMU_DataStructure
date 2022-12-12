# 위상정렬 (topological sorting)
# cycle 없음
# predecessor(선행자) 
# 선(predecessor) = i   후(successor) = j
# i -> j

#ppt 4
# 진입 차수가 없는 그래프 
# 

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

class HeadNode:
    def __init__(self, id_=0, indegree=0):
        self.id_ = id_
        self.indegree = indegree
        self.link = None
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.id_}"
    
class Node:
    def __init__(self, vertex=0):
        self.vertex = vertex
        self.link = None
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.vertex}"
    
class GraphAovBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")
        size = len(mat)
        # Node(i) 는 Adjacency list 의 head 이다.
        list_ = [HeadNode(i) for i in range(size)]
        for row in range(size):
            prev = list_[row]
            for col in range(size):
                if not mat[row][col]:
                    continue
                node = Node(col)
                prev.link = node
                prev = node
                
        return list_
    
class GraphAov:
    def __init__(self, list_, mat):
        self.list_ = list_
        self.mat = mat
        self.__build_indegree()
 
    def indegree(self, v):
        ret = 0
        mat = self.mat
        for row in range(len(mat)):
           ret += mat[row][v]
        return ret
    
    def outdegree(self, v):
        return sum(self.mat[v])
    
    def __build_indegree(self):
        for i, v in enumerate(self):
            v.indegree = self.indegree(i)
    
    def sort_topology(self):
        ret = []  # for return
        # list_ = self.list_
        self.__build_indegree()
        
        stack = Stack()
        
        _ = [stack.push(v) for v in self.list_ if v.indegree == 0]
        
        # for i in list_:
        #     if i.indegree == 0:
        #         stack.push(i)
        
        
        while not stack.is_empty():
            # node = stack.peek()
            head = stack.peek()
            stack.pop()
            ret.append(head)
            
            node = head.link
            # while node.link != None:
            #     node = node.link
            #     list_[node.vertex].indegree -= 1
            #     if list_[node.vertex].indegree == 0:
            #         stack.push(list_[node.vertex])
            while node != None:
                head = self[node.vertex]
                head.indegree -= 1
                if head.indegree == 0:
                    stack.push(head)
                node = node.link
            
        return ret
    
    def __getitem__(self, index):
        return self.list_[index]
    
    def __setitem__(self, index, value):
        self.list_[index] = value
    
    def __len__(self):
        return len(self.list_)
    
    def __str__(self):
        ret = ""
        for i, vt in enumerate(self):
            indegree = vt.indegree
            ret += f"v[{i}: {indegree}] = "
            if vt is None or vt.link is None:
                ret += str(None) + "\n"
                continue
        
            vt = vt.link
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret

def read_input(name_file="input.dat"):
    mat = []
    with open(name_file) as f:
        for line in f:
            (*row,) = map(int, line.split())
            mat.append(row)
    return mat

def print_mat(mat):
    rows, cols = len(mat), len(mat[0])
    for row in range(rows):
        for col in range(cols):
            print(f"{mat[row][col]}", end=" ")
        print("\b")

if __name__ == "__main__":
    mat_ = read_input(r"C:\Users\wsx21\OneDrive\School\3-2\자료구조\lab\lab_22\input_aov_00.dat")
    print("Input matrix:")
    print_mat(mat_)
   
    print()
    print("Adjacency list:")
    list_ = GraphAovBuilder.build(mat_)
    graph = GraphAov(list_, mat_)
    print(graph)
   
    for i in range(len(graph)):
        print(f"v[{i}].outdegree = {graph.outdegree(i)}")
        print(f"v[{i}].indegree = {graph.indegree(i)}")
   
    print()
    print("Topology sorted:")
    topology = graph.sort_topology()
    print(topology)