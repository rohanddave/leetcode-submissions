class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        all_chars = set(s)
        window = collections.defaultdict(int) 
        left = 0
        res = 0

        for right in range(len(s)):
            window[s[right]] += 1

            while window[s[right]] > 2: 
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            # if len(window) == len(all_chars):
            res = max(res, right - left + 1)
        return res