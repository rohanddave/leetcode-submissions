class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drops = 0

        for i in range(1, n): 
            if nums[i] < nums[i - 1]:
                drops += 1
            
            if drops > 1:
                return False
        
        # Check circular boundary
        if nums[0] < nums[n - 1]:
            drops += 1
        return drops <= 1
        