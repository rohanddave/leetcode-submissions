class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        @cache
        def dfs(i, j, k):
            # base cases
            if k < 0:
                return False
            if j == len(t):
                remaining = len(s) - i
                return remaining == k
            if i == len(s):
                remaining = len(t) - j
                return remaining == k

            # if characters match 
            if s[i] == t[j]:
                return dfs(i + 1, j + 1, k)

            insert = dfs(i, j + 1, k - 1)
            delete = dfs(i + 1, j, k - 1)
            replace = dfs(i + 1, j + 1, k - 1)
            return insert or delete or replace
        return dfs(0, 0, 1)