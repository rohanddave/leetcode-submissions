class Solution:
    def maximumMinutes(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fire_spread = [[float('inf') for _ in range(n)] for _ in range(m)]

        q = collections.deque() 

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    fire_spread[i][j] = 0
        
        while q: 
            r, c, time = q.popleft() 

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if (
                    0 <= nr < m and 0 <= nc < n and 
                    grid[nr][nc] == 0 and
                    fire_spread[nr][nc] == float('inf')
                ):
                    q.append((nr, nc, time + 1))
                    fire_spread[nr][nc] = time + 1
        
        def can(wait): 
            nonlocal m, n
            q = collections.deque([(0, 0, wait)]) 
            visited = {(0, 0)}

            while q: 
                r, c, time = q.popleft() 

                if r == m - 1 and c == n - 1: 
                    return True
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc 
                    if (
                        not (0 <= nr < m and 0 <= nc < n) or 
                        grid[nr][nc] == 2 or grid[nr][nc] == 1 or 
                        (nr, nc) in visited
                    ):
                        continue
                    
                    new_time = time + 1
                    if nr == m - 1 and nc == n - 1:
                        if new_time <= fire_spread[nr][nc]:
                            return True
                    elif new_time < fire_spread[nr][nc]:
                        q.append((nr, nc, new_time))
                        visited.add((nr, nc))
            return False
        
        l, r = 0, 10 ** 9 + 1
        while l < r: 
            mid = (l + r) // 2
            if not can(mid): 
                r = mid
            else:
                l = mid + 1
        return l - 1
