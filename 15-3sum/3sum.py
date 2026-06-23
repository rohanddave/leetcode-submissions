class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums) 
        res = []

        for i in range(n): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            target = -nums[i] 
            l, r = i + 1, n - 1
            while l < r: 
                curr = nums[l] + nums[r]
                if curr < target: 
                    l += 1
                elif curr > target: 
                    r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1

                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1
        return res
        