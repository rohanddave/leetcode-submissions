class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        memo = {}
        def dfs(i, target): 
            if target == 0: 
                return True 
            if target < 0 or i == len(nums): 
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            
            skip = dfs(i + 1, target)
            memo[(i, target)] = skip
            if skip:
                return skip
            if nums[i] <= target: 
                pick = dfs(i + 1, target - nums[i])
                memo[(i, target)] = memo[(i, target)] or pick
            
            return memo[(i, target)]
        return dfs(0, total // 2)
        