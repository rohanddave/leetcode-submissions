class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        observations: 
        - all elements except one appear EXACTLY twice 
        - hence the size of the array is always odd, n - 1 * 2 (even) + 1 = odd 


        example:
        [1,1,2,3,3,4,4,8,8]
        '''

        l, r = 0, len(nums) - 1
        while l < r: 
            m = (l + r) // 2
            if (m % 2 == 1 and nums[m - 1] == nums[m]) or (m % 2 == 0 and nums[m] == nums[m + 1]):
                l = m + 1
            else:
                r = m
        return nums[l]



        
            