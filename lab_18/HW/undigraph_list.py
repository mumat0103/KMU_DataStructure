#20180269 천성규
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
    def __str__(self):
        return f"{self.data}"
    
class UndiGraph:
    def __init__(self, mat):
        self.mat = mat
        self.vertices = len(mat)
        self.linked = [None] * self.vertices
        self.__build()
    
    def __build(self):
        size = len(mat)
        for row in range(size):
            prev = self.linked[row]
            for col in range(size):
                if not self.mat[row][col]:
                    continue
                node = Node(col)
                if prev is None:
                    self.linked[row] = node
                else:
                    prev.link = node
                prev = node

    def add_edge(self, src, dst):
        if self.linked[src] is None:
            self.linked[src] = Node(dst)
            return

        vt = self.linked[src]
        temp = self.linked[src]
  
        while temp is not None:
            vt = temp
            temp = temp.link

        vt.link = Node(dst)
       
    
    def __str__(self):
        ret = ""
        for i, vt in enumerate(self.linked):
            ret += f"v[{i}] = "
            if vt is None:
                ret += "None\n"
                continue
            
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
    mat = read_input(r"C:\Users\wsx21\OneDrive\School\3-2\자료구조\lab\lab_18\HW\input_g4.dat")
    print("Input matrix")
    print_mat(mat)
    print()
    print("Adjacency list")
    graph = UndiGraph(mat)
    print(graph)
