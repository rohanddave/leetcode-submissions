class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()

        @cache
        def dfs(i):
            if i >= len(rides):
                return 0 
            
            skip = dfs(i + 1)
            start, end, tip = rides[i] 
            l, r = i + 1, len(rides) 
            while l < r:
                m = (l + r) // 2
                if rides[m][0] >= end: 
                    r = m 
                else:
                    l = m + 1

            pick =  end - start + tip + dfs(l)
            return max(pick, skip)
        return dfs(0)
        