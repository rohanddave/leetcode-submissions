class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums) 

        if total_sum % k != 0:
            return False

        initial_mask = 0 
        target = total_sum // k 
        memo = {}
        def dfs(mask, curr_sum): 
            nonlocal target
            if mask == (1 << len(nums)) - 1:
                return curr_sum == 0
            if (mask, curr_sum) in memo: 
                return memo[(mask, curr_sum)]
            
            for i in range(len(nums)): 
                if mask & (1 << i) or curr_sum + nums[i] > target: 
                    continue
                
                prev_mask = mask 
                new_mask = mask | (1 << i)
                new_sum = curr_sum + nums[i]
                pick = dfs(new_mask, new_sum if new_sum != target else 0)
                if pick:
                    memo[(mask, curr_sum)] = True
                    return memo[(mask, curr_sum)]
                mask = prev_mask
                
            memo[(mask, curr_sum)] = False
            return memo[(mask, curr_sum)]
        return dfs(initial_mask, 0)

        