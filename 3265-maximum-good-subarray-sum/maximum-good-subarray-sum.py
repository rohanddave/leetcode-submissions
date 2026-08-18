class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        hashmap = collections.defaultdict(lambda: float('inf'))
        res = float('-inf')
        for i in range(len(nums)):
            if nums[i] - k in hashmap: 
                res = max(res, prefix[i + 1] - hashmap[nums[i] - k])
            if nums[i] + k in hashmap: 
                res = max(res, prefix[i + 1] - hashmap[nums[i] + k])
            hashmap[nums[i]] = min(hashmap[nums[i]], prefix[i])
        
        return res if res != float('-inf') else 0




        