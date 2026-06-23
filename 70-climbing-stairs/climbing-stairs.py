class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i): 
            if i == n: 
                return 1
            if i in memo:
                return memo[i]
            
            one = dfs(i + 1) 
            two = 0 if i + 2 > n else dfs(i + 2)
            memo[i] = one + two 
            return memo[i]
        return dfs(0)

        