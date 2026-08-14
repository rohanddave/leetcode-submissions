class Solution:
    def minOperations(self, nums: list[int]) -> int:
        '''
        problem: 
        - increase each element nums[l...r] by x (positive number)
        - minimum sum of values of x to make nums non decreasing 

        goal: return min sum of x across all ops to make array non-decreasing


        observations: 
        - x is positive so the value of nums[i] can only increase
        - non-decreasing means nums[i] <= nums[i + 1] i.e. last element should be the largest

        scan left to right till nums[i] <= nums[i + 1] <= nums[i + 2]
        nums[0] <= nums[1]

        nums[i] >= nums[i - 1]
        nums[1] >= nums[0]

        non-decreasing = prev element smaller or equal to next / next element greater or equal to prev

        example:
        [5,1,2,3,9,1,2,3]
        for subarray of indices [1,2,3] to be non decreasing index 1 has to be atleast equal index 0
        so x = nums[0] - nums[1] = 4
        [5,5,6,7,9,1,2,3]
        next x = 8
        [5,5,6,7,9,9,10,11]
        res = 12
        '''
        res = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                res += nums[i - 1] - nums[i]
        return res

        return res