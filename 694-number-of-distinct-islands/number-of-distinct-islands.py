class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        target_row = r + trans_dr
        trans_dr = target_row - r
        '''
        m, n = len(grid), len(grid[0])
        distinct_islands = set()

        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1: 
                    island_start = (i, j)
                    trans_dr, trans_dc = -i, -j

                    island = [] 
                    q = collections.deque([island_start])
                    grid[i][j] = 0

                    while q: 
                        r, c = q.popleft()

                        translated_r, translated_c = r + trans_dr, c + trans_dc
                        island.append((translated_r, translated_c)) 

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc 
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1: 
                                q.append((nr, nc))
                                grid[nr][nc] = 0

                    distinct_islands.add(tuple(island))

        return len(distinct_islands)
        
        