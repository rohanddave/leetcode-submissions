class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([(0, 0, 0)])
        visited = {(0, 0)}

        while q:
            removals, r, c = q.popleft() 

            if r ==  m - 1 and c == n - 1:
                return removals 
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if grid[nr][nc] == 0:
                        q.appendleft((removals + grid[nr][nc], nr, nc))
                    else:
                        q.append((removals + grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
        