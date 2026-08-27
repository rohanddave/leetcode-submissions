class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        seen[0] = 1
        curr, count = 0, 0
        for i, num in enumerate(nums): 
            curr += num 
            count += seen[curr - k]
            seen[curr] += 1
        return count