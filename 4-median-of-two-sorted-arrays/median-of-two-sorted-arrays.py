class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total_length = len(A) + len(B) 
        half_length = total_length // 2

        left, right = 0, len(A)
        while True: 
            i = (left + right) // 2
            j = half_length - i
            
            left_A = A[i - 1] if (i - 1)>= 0 else float('-inf')
            right_A = A[i] if i < len(A) else float('inf')
            left_B = B[j - 1] if (j - 1) >= 0 else float('-inf')
            right_B = B[j] if j < len(B) else float('inf')

            if left_A <= right_B and left_B <= right_A:
                # calculate median 
                if total_length % 2 == 0:
                    return (max(left_A, left_B) + min(right_A, right_B)) / 2
                return min(right_A, right_B)
            if left_A > right_B: 
                right = i - 1
            else:
                left = i + 1







        