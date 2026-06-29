class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        nums = [5, 2, 3, 4, 3]
        out  = [-1, 3, 4, 5, 5]

        [5, 2, 3, 4, 3][5, 2, 3, 4, 3]
        res = [-1, 3, 4, -1, 5]
        stack = [5, 4, 3]
        '''
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range((2 * n) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            
            if stack:
                res[i % n] = nums[stack[-1]]
            
            stack.append(i % n)
        return res

        