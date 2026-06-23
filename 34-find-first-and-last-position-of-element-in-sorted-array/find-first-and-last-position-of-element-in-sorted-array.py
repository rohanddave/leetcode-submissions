class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        first index: bin search for last less than target; find first gte
        last index: bin search for first greater than target
        '''
        l, r = 0, len(nums)
        res = [] 
        while l < r: 
            m = (l + r) // 2
            if nums[m] >= target: 
                r = m 
            else: 
                l = m + 1

        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        
        res.append(l)
        
        l, r = 0, len(nums)
        while l < r: 
            m = (l + r) // 2
            if nums[m] > target: 
                r = m
            else: 
                l = m + 1

        res.append(l - 1)
        return res
        
        