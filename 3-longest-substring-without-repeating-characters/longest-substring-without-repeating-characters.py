class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_count = collections.defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):
            window_count[s[right]] += 1

            while window_count[s[right]] > 1: 
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
        