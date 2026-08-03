class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = collections.defaultdict(int)
        max_length = 0 
        left = 0 

        for right in range(len(s)): 
            window[s[right]] += 1

            while len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        return max_length