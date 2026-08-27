class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l = 0
        window = collections.defaultdict(int)

        for r in range(len(s)): 
            window[s[r]] += 1

            while window and window[s[r]] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            res = max(res, r - l + 1)
        return res
        