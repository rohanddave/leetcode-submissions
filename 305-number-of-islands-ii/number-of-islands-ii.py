class UnionFind: 
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = 0 
        self.size = [0] * n
    
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
        # px is always greater 
        self.size[px] += self.size[py]
        self.parent[py] = px
        self.components -= 1
        return True
    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)

        def get_id(r, c): 
            return r * n + c
        
        answers = []

        land_cells = set()

        for (r, c) in positions:
            # forms an island at r, c
            if (r, c) in land_cells:
                answers.append(uf.components)
                continue
            uf.components += 1
            uf.size[get_id(r, c)] = 1
            land_cells.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) in land_cells: 
                    uf.union(get_id(r, c), get_id(nr, nc))
            answers.append(uf.components)
        return answers

        