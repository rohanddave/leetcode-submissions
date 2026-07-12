class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        

        def bfs(r, c): 
            q = collections.deque([(0, r, c)])
            visited = {(r, c)}

            while q: 
                curr_dist, curr_r, curr_c = q.popleft() 

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = curr_r + dr, curr_c + dc 
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                        q.append((curr_dist + 1, nr, nc))
                        visited.add((nr, nc))
                        count[nr][nc] += 1
                        dist[nr][nc] += curr_dist + 1

        number_of_buildings = 0

        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1:
                    number_of_buildings += 1
                    bfs(i, j)
        
        res = float('inf')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and count[i][j] == number_of_buildings:
                    res = min(res, dist[i][j])
        
        return res if res != float('inf') else -1