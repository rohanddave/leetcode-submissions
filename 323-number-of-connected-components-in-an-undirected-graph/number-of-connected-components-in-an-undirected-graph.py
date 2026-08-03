class UnionFind: 
    def __init__(self, n): 
        self.size = [1] * n 
        self.parent = list(range(n))
        self.components = n 
    
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 
    
    def union(self, x, y): 
        px, py = self.find(x), self.find(y)
        if px == py: 
            return False 
        
        if self.size[px] < self.size[py]:
            px, py = py, px 
        self.size[px] += self.size[py]
        self.parent[py] = px
        self.components -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges: 
            uf.union(a, b)
        return uf.components