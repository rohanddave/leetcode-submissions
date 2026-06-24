class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right: 
            m = (left + right) // 2
            if arr[m] > arr[m + 1]:
                right = m 
            else:
                left = m + 1
        return left