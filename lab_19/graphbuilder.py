class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
    def __str__(self):
        return f"{self.data}"

class GraphBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")
        size = len(mat)
        ret = [None] * size
        for row in range(size):
            for col in range(size):
                if not mat[row][col]:
                    continue
                node = Node(col)
                node.link = ret[row]
                ret[row] = node
            
        return ret
    
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
    
if __name__ == "__main__":
    mat = [[0, 1, 1, 1], 
           [1, 0, 1, 1], 
           [1, 1, 0, 1], 
           [1, 1, 1, 0]]
    
    graph = GraphBuilder.build(mat)
    print(graph)
