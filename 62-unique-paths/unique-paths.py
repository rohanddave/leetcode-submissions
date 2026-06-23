class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0 
            if (i, j) in memo:
                return memo[(i, j)]
            
            count = 0 
            for di, dj in [(1, 0), (0, 1)]:
                count += dfs(i + di, j + dj)
            
            memo[(i, j)] = count
            
            return count
        
        return dfs(0, 0)
        
        