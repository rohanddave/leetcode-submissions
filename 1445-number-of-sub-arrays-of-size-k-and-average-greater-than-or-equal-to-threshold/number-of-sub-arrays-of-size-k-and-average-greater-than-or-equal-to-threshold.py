class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0 
        l = 0
        window_sum = 0

        for r in range(len(arr)): 
            window_sum += arr[r]

            if r < k - 1: 
                continue
            
            avg = window_sum / k
            if avg >= threshold:
                count += 1
            window_sum -= arr[l]
            l += 1
        return count

        