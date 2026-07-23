class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        '''
        problem: 
        - m x n grid 
        - n balls 
        - 

        observations: 
        - one ball per column 
        - if a ball has reached col = 0 or col = n - 1 and row != m - 1 then it has touched a wall and will never reach the bottom 
        - if two balls cross each other then that forms a V and hence those will never reach the bottom 

        example: 
        grid = [
        [1,1,1,0,0],
        [1,1,1,0,0],
        [0,0,0,1,1],
        [1,1,1,1,0],
        [0,0,0,0,0]
        ]
        '''

        m, n = len(grid), len(grid[0])

        ans = [-1] * n

        for i in range(n): 
            curr_col = i
            stuck = False
            for row in range(m): 
                next_col = curr_col + grid[row][curr_col]
                if next_col < 0 or next_col >= n or grid[row][curr_col] != grid[row][next_col]:
                    stuck = True 
                    break
                curr_col = next_col
            if not stuck:
                ans[i] = curr_col
        return ans
            