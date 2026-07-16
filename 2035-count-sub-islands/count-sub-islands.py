class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        goal: return number of islands in grid2 that are sub islands 

        problem: 
        - subisland = island in grid 2 such that island in grid1 containing all cells 

        observations: 
        - do a bfs on grid2 exploring only 1's
        - if any r,c for island in grid2 is != 1 in grid1 then this is not a subisland
        - q only holds (r, c) in grid2
        - visited set only holds (r, c) of grid2 
        '''
        m, n = len(grid1), len(grid1[0])

        q = collections.deque() 
        visited = set() 

        count = 0

        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and (r, c) not in visited: 
                    q.append((r, c))
                    visited.add((r, c))

                    is_subisland = grid1[r][c] == 1

                    while q: 
                        curr_r, curr_c = q.popleft() 

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid2[nr][nc] == 1: 
                                if grid1[nr][nc] != 1: 
                                    is_subisland = False 
                                q.append((nr, nc))
                                visited.add((nr, nc))

                    if is_subisland:
                        count += 1
        return count

        