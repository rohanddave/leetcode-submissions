class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = float('inf')
        closest_sum = None

        for i in range(n): 
            l, r = i + 1, n - 1
            while l < r: 
                curr_sum = nums[i] + nums[l] + nums[r]
                diff = target - curr_sum
                abs_diff = abs(diff) 
                if abs_diff < min_diff:
                    min_diff = abs_diff
                    closest_sum = curr_sum
                
                if curr_sum < target: 
                    l += 1
                elif curr_sum > target: 
                    r -= 1
                else: 
                    return target
                

        return closest_sum
