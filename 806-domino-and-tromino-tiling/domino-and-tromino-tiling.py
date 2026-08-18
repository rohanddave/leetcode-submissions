class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, gap): 
            if i == n: 
                return 1 if gap == 0 else 0
            if i > n:
                return 0 
            
            if gap == 0:
                vertical = dfs(i + 1, 0)
                two_horizontal = dfs(i + 2, 0)
                tromino = dfs(i + 1, 1)
                return (vertical + two_horizontal + tromino) % MOD

            domino = dfs(i + 1, 1)
            tromino = 2 * dfs(i + 2, 0)
            return (domino + tromino) % MOD 
        
        return dfs(0, 0)

        