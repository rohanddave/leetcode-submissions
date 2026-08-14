from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b): 
            if int(a + b) > int(b + a): 
                return -1
            elif int(a + b) < int(b + a):
                return 1
            return 0
        
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))
        res_str = ''.join(nums_str)
        counter = collections.Counter(res_str)
        return '0' if len(counter) == 1 and '0' in counter else res_str
        