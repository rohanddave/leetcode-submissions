class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        window_size, window_latest = 0, float('-inf')
        res = float('-inf')

        for r in range(n):
            # if not strictly increasing
            if nums[r] <= window_latest:
                window_size = 1
                window_latest = nums[r]
            else: 
                window_size += 1
                window_latest = nums[r]
            res = max(res, window_size)
        
        window_size, window_latest = 0, float('inf')
        for r in range(n):
            if nums[r] >= window_latest: 
                window_size = 1
                window_latest = nums[r]
            else: 
                window_size += 1
                window_latest = nums[r]
            res = max(res, window_size)
        return res
