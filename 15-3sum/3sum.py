class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r: 
                curr_sum = nums[i] + nums[l] + nums[r] 
                if curr_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res 

        