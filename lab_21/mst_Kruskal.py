#20180269 천성규
class Edge:
    def __init__(self, u, v, w):
        self.u = u # head
        self.v = v # tail
        self.w = w # weight
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.u, self.v, self.w}"
    
class Graph:
    def __init__(self, mat):
        self.mat = mat
        self.list_ = []
        self.__build()
        
    def __build(self):
        for r in range(len(self.mat)):
            for c in range(len(self.mat[0])):
                if not self.mat[r][c]:
                    continue
                if c <= r:
                    continue
                self.list_.append(Edge(r, c, self.mat[r][c]))
                
    def __iter__(self):
        return iter(self.list_)
    
    def find(self, parent, i):
        while parent[i] >= 0:
            i = parent[i]
        return i
   
    def union(self, parent, count, i, j):
        temp = parent[i] + parent[j]
        if parent[i] > parent[j]:
            parent[i] = j
            parent[j] = temp
        else:
            parent[j] = i
            parent[i] = temp
    
    def kruskal(self):
        ret = []
        self.list_.sort(key=lambda edge: edge.w)
        size = len(self.mat)
        
        parent = [-1] * size
        count = [-1] * size

        i = 0
        e = 0
        
        while e < size - 1:
            edge = self.list_[i]
            parent_u = self.find(parent, edge.u)
            parent_v = self.find(parent, edge.v)

            if parent_u != parent_v:
                ret.append(edge)
                self.union(parent, count, parent_u, parent_v)
                e += 1
                
            i += 1
        
        if e < size - 1:
            return []
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
    mat_ = read_input(r"C:\Users\wsx21\OneDrive\School\3-2\자료구조\lab\lab_21\input_g1.dat")
    print("Input matrix:")
    print_mat(mat_)
    print()
    
    graph = Graph(mat_)
    print(graph.list_)
    
    print()
    print("edges:")
    for i in graph:
        print(i)
        
    print()
    print("Kruskal's Algorithm:")
    mst = graph.kruskal()
    for i in mst:
        print(i)