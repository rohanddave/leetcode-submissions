class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for start_idx, end_idx in queries: 
            diff[start_idx] -= 1
            diff[end_idx + 1] += 1
        
        running_diff = 0 
        for i in range(n): 
            running_diff += diff[i] 
            if nums[i] + running_diff > 0:
                return False
        return True

        