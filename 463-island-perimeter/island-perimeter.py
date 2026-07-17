class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1: 
                    q = collections.deque([(i, j)]) 
                    visited = {(i, j)}
                    perimeter = 0 

                    while q: 
                        r, c = q.popleft() 

                        peri_contr = 4

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                if (nr, nc) not in visited:
                                    q.append((nr, nc))
                                    visited.add((nr, nc))
                                peri_contr -= 1
                        perimeter += peri_contr

                    return perimeter

        