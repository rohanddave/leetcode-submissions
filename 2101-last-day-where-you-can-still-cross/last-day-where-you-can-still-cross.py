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
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        self.components -= 1
        return True

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        '''
        observations: 
        - there is no explicit matrix to work on 
        - left to right UF will not work since we would need a un-union operation
        - left to right binary search will not work unless all cells before the current position are considered
        - all we care about is connectivity not the path itself, makes UF a strong candidate 

        approach: 
        - iterate from the end of cells 
        - prepare a UF data structure and union all (r,c) with nei 0 cells 
        - 
        '''
        TOP_PARENT, BOTTOM_PARENT = (row * col), (row * col) + 1
        n = (row * col) + 2
        uf = UnionFind(n)
        def get_id(r, c): 
            nonlocal row, col
            return r * col + c
        
        land = set() 

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i]
            r -= 1
            c -= 1

            land.add((r, c))

            if r == 0:
                uf.union(get_id(r, c), TOP_PARENT)
            if r == row - 1: 
                uf.union(get_id(r, c), BOTTOM_PARENT)
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                # within bounds and nei is not obstacle
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) in land:
                    uf.union(get_id(r, c), get_id(nr, nc))
            
            if uf.find(TOP_PARENT) == uf.find(BOTTOM_PARENT):
                return i
        
