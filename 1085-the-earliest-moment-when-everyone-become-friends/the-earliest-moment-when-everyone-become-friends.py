class UnionFind:
    def __init__(self, n): 
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n 
    
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): 
        px, py = self.find(x), self.find(y)
        if px == py:
            return False 
        
        if px < py: 
            px, py = py, px 
        self.size[px] += self.size[py]
        self.parent[py] = px
        self.components -= 1
        return True 
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        '''
        observations: 
        - a friends with b means b friends with a too (symmetric)
        - a acquainted with b if a is friends with b or a is friend with acquaintance of b
        '''
        uf = UnionFind(n)
        res = None
        for timestamp, a, b in sorted(logs):
            if uf.union(a, b):
                res = timestamp 
        return res if uf.components == 1 else -1

            
