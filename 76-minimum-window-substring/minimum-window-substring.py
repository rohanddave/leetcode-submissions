class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        have, need = 0, len(t_count)
        window = collections.defaultdict(int)
        l, min_length = 0, float('inf')
        res = '' 

        for r in range(len(s)): 
            window[s[r]] += 1
            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                have += 1

            while l <= r and have == len(t_count): 
                if (r - l + 1) < min_length: 
                    res = s[l: r + 1]
                    min_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        return res


