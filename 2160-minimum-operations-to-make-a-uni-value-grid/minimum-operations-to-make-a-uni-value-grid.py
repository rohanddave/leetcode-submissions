class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        '''
        goal: return min number of operations to make grid uni value. -1 if not possible 

        problem: 
        - m x n grid 
        - allowed to add x or subtract x from any element 

        observation: 
        - which number to choose to try to make each cell? 
        - does that number necessarily lie in the values of the matrix? 
        - maybe the middle element in sorted order? since ~n/2, n/2 - 1 elements are at most nums[mid] - nums[0] + nums[mid] - nums[-1] 
        - operations for a cell to reach target = abs(mat[i][j] - target) / x
        - 
        
        example: 
        Input: grid = [[2,4],[6,8]], x = 2
        Output: 4

        sorted order = [2, 4, 6, 8]

        '''
        m, n = len(grid), len(grid[0])

        nums = []
        for row in grid:
            nums.extend(row)

        nums.sort()

        target = nums[len(nums) // 2]
        rem = nums[0] % x
        res = 0
        for i in range(len(nums)):
            if nums[i] % x != rem:
                return -1
            res += abs(target - nums[i]) // x
        return res
