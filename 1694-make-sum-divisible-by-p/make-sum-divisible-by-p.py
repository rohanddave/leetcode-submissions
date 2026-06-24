class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        hashmap = {0: -1}
        prefix = 0
        res = len(nums)
        for j in range(len(nums)): 
            prefix = (prefix + nums[j]) % p
            remaining = (prefix - target) % p
            if remaining in hashmap: 
                res = min(res, j - hashmap[remaining])
            hashmap[prefix] = j
        return res if res < len(nums) else -1


        