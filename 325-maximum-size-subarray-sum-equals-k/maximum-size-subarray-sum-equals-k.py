class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixes = {}
        prefixes[0] = -1
        curr_sum = 0
        max_length = 0
        for i, num in enumerate(nums): 
            curr_sum += num 
            target = curr_sum - k 
            if target in prefixes:
                max_length = max(max_length, i - prefixes[target])
            if curr_sum not in prefixes:
                prefixes[curr_sum] = i 


        return max_length