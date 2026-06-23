class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def dfs(r, c): 
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if r == m or c == n:
                return float('inf')
            if (r, c) in memo: 
                return memo[(r, c)]
            
            down = grid[r][c] + dfs(r + 1, c)
            right = grid[r][c] + dfs(r, c + 1) 
            memo[(r, c)] = min(down, right)
            return memo[(r, c)]
        return dfs(0, 0)