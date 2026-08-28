class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j): 
            if i == m - 1 and j == n - 1:
                return 1 
            if not (0 <= i < m) or not (0 <= j < n):
                return 0
            
            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            return down + right
        return dfs(0, 0)
        