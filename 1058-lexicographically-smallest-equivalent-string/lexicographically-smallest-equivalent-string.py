class UnionFind: 
    def __init__(self, n): 
        self.parent = list(range(n))
    
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): 
        px, py = self.find(x), self.find(y) 
        if px == py:
            return False 
        
        # ensure px is smaller
        if px > py: 
            px, py = py, px 
        
        # attach py to px
        self.parent[py] = px 
        return True 
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for i in range(len(s1)): 
            x, y = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            uf.union(x, y)
        
        res = [] 
        for char in baseStr: 
            smallest = uf.find(ord(char) - ord('a'))
            res.append(chr(ord('a') + smallest))
        
        return ''.join(res)
