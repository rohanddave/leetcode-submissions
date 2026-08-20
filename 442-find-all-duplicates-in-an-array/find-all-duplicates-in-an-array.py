class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums): 
            pos = abs(num) - 1
            if nums[pos] < 0: 
                res.append(abs(num))
            else: 
                nums[pos] *= -1
        return res

        