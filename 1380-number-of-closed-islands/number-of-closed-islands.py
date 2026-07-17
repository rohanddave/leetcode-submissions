class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        problem: 
        - 0 = land and 1 = water 
        - closed island = island that is surrounded by water on all 4 sides 

        goal: return number of closed islands 

        observations: 
        - if the island has a point touching the edge of the grid then not a closed island 
        
        approach: 
        approach 1:
        - count number of islands
        - subtract count of number of islands from edge from the total count
        

        approach 2: 
        - when exploring an island if a point touches the edge then do not count that island in the total count as this is not a closed island
        '''

        m, n = len(grid), len(grid[0])
        count = 0 
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 0: 
                    q = collections.deque([(i, j)]) 
                    is_closed = True

                    while q: 
                        r, c = q.popleft() 

                        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                            is_closed = False

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc 
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0: 
                                q.append((nr, nc))
                                grid[nr][nc] = 1

                    count += 1 if is_closed else 0                            
        
        return count