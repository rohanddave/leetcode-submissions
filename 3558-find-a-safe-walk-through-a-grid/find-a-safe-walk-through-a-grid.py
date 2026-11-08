class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        max_health = [[float('-inf') for _ in range(n)] for _ in range(m)]
        initial_health = health - grid[0][0]
        max_health[0][0] = initial_health
        q = collections.deque([(initial_health, 0, 0)])

        while q: 
            curr_health, r, c = q.popleft()

            if curr_health < max_health[r][c]:
                continue 
            
            if r == m - 1 and c == n - 1:
                return True 
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n: 
                    new_health = curr_health - grid[nr][nc]
                    if new_health <= 0:
                        continue

                    if new_health > max_health[nr][nc]:
                        max_health[nr][nc] = new_health
                        if grid[nr][nc] == 0:
                            q.appendleft((new_health, nr, nc))
                        else: 
                            q.append((new_health, nr, nc))
            
        return False
        