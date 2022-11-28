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
        
class NodeEdge:
    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head
        self.link_tail = None
        self.link_head = None #indegree
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"({self.tail}:{self.head}:{self.link_head}:{self.link_tail})"
    
class GraphOrtho:
    def __init__(self, heads=None):
        self.heads = heads
    
    def is_empty(self):
        return not self.heads
    
    def outdegree(self, v):
        sum_ = 0
        node = self.heads[v].link_tail
        while node is not None:
            sum_ += 1
            node = node.link_tail
        
        return sum_
    
    def indegree(self, v):
        sum_ = 0
        node = self.heads[v].link_head
        while node is not None:
            sum_ += 1
            node = node.link_head
        return sum_


class GraphOrthoBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")
        size = len(mat)
        ret = [NodeEdge(tail=i) for i in range(size)] #vertax

        for row in range(size):
            for col in range(size):
                if not mat[row][col]:
                    continue
                
                node = NodeEdge(tail=row, head=col)
                node.link_tail = ret[row].link_tail
                node.link_head = ret[col].link_head
                ret[row].link_tail = node
                ret[col].link_head = node
                
        return ret
    
if __name__ == "__main__":
    mat_ = read_input(r"C:\Users\wsx21\OneDrive\School\3-2\자료구조\lab\lab_19\input_g3.dat")
    print("Input matrix")
    print_mat(mat_)
    heads_ = GraphOrthoBuilder.build(mat_)
    graph = GraphOrtho(heads_)
    print()
    print(graph.heads[0].link_tail)
    print(graph.heads[1].link_tail)
    print(graph.heads[2].link_tail)
    print()
    print(graph.heads[0])
    print(graph.heads[1])
    print(graph.heads[2])
    print()
    v = 0
    print(f"outdegree[{v}] =", graph.outdegree(v))
    print(f"indegree[{v}] =", graph.indegree(v))
    v = 1
    print(f"outdegree[{v}] =", graph.outdegree(v))
    print(f"indegree[{v}] =", graph.indegree(v))
    v = 2
    print(f"outdegree[{v}] =", graph.outdegree(v))
    print(f"indegree[{v}] =", graph.indegree(v))