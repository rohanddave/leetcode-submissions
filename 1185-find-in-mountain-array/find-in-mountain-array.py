# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def get_peak_index():
            left, right = 0, mountainArr.length() - 1
            while left < right: 
                m = (left + right) // 2
                if mountainArr.get(m) > mountainArr.get(m + 1): 
                    right = m 
                else:
                    left = m + 1
            return left 
        
        def left_search(l, r): 
            left, right = l, r
            while left <= right:
                m = (left + right) // 2
                if mountainArr.get(m) == target:
                    return m
                elif target < mountainArr.get(m): 
                    right = m - 1
                else:
                    left = m + 1
            return -1
        
        def right_search(l, r): 
            left, right = l, r 
            while left <= right: 
                m = (left + right) // 2
                if mountainArr.get(m) == target:
                    return m
                elif target < mountainArr.get(m): 
                    left = m + 1
                else:
                    right = m - 1
            return -1
        
        peak_index = get_peak_index()

        left_res = left_search(0, peak_index)
        right_res = right_search(peak_index + 1, mountainArr.length() - 1)
        if left_res != -1:
            return left_res
        if right_res != -1:
            return right_res 
        return -1
        