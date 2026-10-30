class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(start, end): 
            if start >= end:
                return [nums[start]]
            
            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)
            return merge(left, right)
        
        def merge(left, right): 
            res = []
            l, r = 0, 0

            while l < len(left) and r < len(right): 
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else: 
                    res.append(right[r])
                    r += 1
            
            if l < len(left):
                res.extend(left[l:])
            
            if r < len(right):
                res.extend(right[r:])
            
            return res
        
        if not nums:
            return []
            
        return merge_sort(0, len(nums) - 1)

        