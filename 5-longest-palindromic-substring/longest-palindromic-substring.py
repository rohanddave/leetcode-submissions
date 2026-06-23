class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_center(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]: 
                i -= 1
                j += 1
            return s[i + 1: j]
        
        res = ''
        for i in range(len(s)): 
            even = expand_center(i, i + 1)
            if len(even) > len(res):
                res = even
            odd = expand_center(i, i)
            if len(odd) > len(res): 
                res = odd
        return res
        