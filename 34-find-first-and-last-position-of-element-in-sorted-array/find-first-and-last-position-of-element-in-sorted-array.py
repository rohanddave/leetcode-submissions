class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n
        while l < r: 
            m = (l + r) // 2
            if nums[m] >= target: 
                r = m 
            else: 
                l = m + 1
        
        if l >= n or nums[l] != target:
            return [-1, -1]

        res = [l] 

        l, r = 0, n 
        while l < r: 
            m = (l + r) // 2
            if nums[m] > target: 
                r = m
            else:
                l = m + 1
        
        res.append(l - 1)
        return res
        