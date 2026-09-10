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
        return True 

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)

        for i in range(n - 1): 
            if abs(nums[i] - nums[i + 1]) <= maxDiff:
                uf.union(i, i + 1)
        
        res = []

        for a, b in queries: 
            res.append(uf.find(a) == uf.find(b))
        
        return res
                

        