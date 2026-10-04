class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        positive_ptr, negative_ptr = 0, 1

        for i in range(n): 
            if nums[i] > 0:
                res[positive_ptr] = nums[i]
                positive_ptr += 2
            else: 
                res[negative_ptr] = nums[i]
                negative_ptr += 2
        return res
        