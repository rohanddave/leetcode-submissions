class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_so_far = 0 
        prev_element = 0

        for num in arr: 
            missing_so_far += num - prev_element - 1
            prev_element = num
            if missing_so_far >= k: 
                extra = missing_so_far - k
                return num - extra - 1

        required = k - missing_so_far 
        return arr[-1] + required  
        

        

        