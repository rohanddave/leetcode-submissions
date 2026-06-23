class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        dfs fn returns the number of ways to reach m - 1, n - 1 from r, c
        '''
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        memo = {}
        def dfs(r, c): 
            if r == m - 1 and c == n - 1:
                return 1 
            if r == m or c == n:
                return 0
            if (r, c) in memo: 
                return memo[(r, c)]
            
            ways = 0
            if r + 1 < m and obstacleGrid[r + 1][c] == 0:
                ways += dfs(r + 1, c)
            if c + 1 < n and obstacleGrid[r][c + 1] == 0:
                ways += dfs(r, c + 1)
            memo[(r, c)] = ways
            return memo[(r, c)]
        return dfs(0, 0)
            