class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        l_max, r_max = 0, 0
        total = 0

        while l < r: 
            if height[l] <= height[r]: 
                if height[l] >= l_max: 
                    l_max = height[l]
                else: 
                    total += l_max - height[l]
                l += 1
            else: 
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    total += r_max - height[r]
                r -= 1
        return total
        