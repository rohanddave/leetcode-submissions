class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        goal: reutrn number of 4 directional walks from starting to end walking over all 0's exactly once 

        approach: 
        - when at r, c explore all 4 direcitonal neighbors 
        - terminating condition: r, c == end and count of 0's == total count of 0's
        - visit a cell and mark as visited -> when entire chain done backtrack and mark as univisted
        '''
        m, n = len(grid), len(grid[0])

        target_count = 0 
        start_pos, end_pos = None, None
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 0:
                    target_count += 1
                elif grid[i][j] == 1:
                    start_pos = (i, j)
                elif grid[i][j] == 2:
                    end_pos = (i, j)
        
        res = 0
        def dfs(r, c, count): 
            nonlocal end_pos, res
            if (r, c) == end_pos and count == target_count:
                res += 1
                return 
            
            # increment count if the current grid is empty
            prev_count = count
            count += 1 if grid[r][c] == 0 else 0
            # mark cell as visited
            tmp = grid[r][c]
            grid[r][c] = -1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 0:
                        dfs(nr, nc, count)
                    elif grid[nr][nc] == 2 and count == target_count:
                        dfs(nr, nc, count)

            
            # backtrack
            grid[r][c] = tmp
            count = prev_count
        dfs(start_pos[0], start_pos[1], 0)
        return res
            
        