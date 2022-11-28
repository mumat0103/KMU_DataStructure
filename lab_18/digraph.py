class DiGraph:
    def __init__(self, size):
        self.graph = [[0] * size for _ in range(size)]
    
    def insert_edge(self, src, dst, elem=1):
        self.graph[src][dst] = elem
    
    def remove_edge(self, src, dst, elem=0):
        self.graph[src][dst] = elem
    
    def indegree(self, v):
        cnt = 0
        for i in range(len(self)):
            cnt += self[i, v]
        return cnt
    
    def outdegree(self, v):
        return sum(self.graph[v])
    
    def __getitem__(self, coords):
        return self.graph[coords[0]][coords[1]]
    
    def __setitem__(self, coords, elem):
        self.graph[coords[0]][coords[1]] = elem
    
    def __len__(self):
        return len(self.graph)
    
    def __str__(self):
        ret = ""
        for row in range(len(self.graph)):
            ret += str(self.graph[row]) + "\n"
        return ret.strip()

if __name__ == "__main__":
    VERTICES = 3
    graph = DiGraph(VERTICES)
    graph.insert_edge(0, 1)
    graph.insert_edge(1, 0)
    graph[1, 2] = 1
    
    print("graph")
    for row in range(len(graph)):
        for col in range(len(graph)):
            print(graph[row, col], end=" ")
        print()
    
    print()
    v = 1
    print(f"indegree[{v}] = {graph.indegree(v)}")
    print(f"outdegree[{v}] = {graph.outdegree(v)}")
    
    print()
    v = 2
    print(f"indegree[{v}] = {graph.indegree(v)}")
    print(f"outdegree[{v}] = {graph.outdegree(v)}")
    
    print()
    print("graph")
    print(graph)
