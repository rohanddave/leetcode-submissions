class Solution:
    def numWays(self, n: int, k: int) -> int:
        '''
        at each fence we can pick k colors if the streak is < 2 else k - 1 colors
        '''
        memo = {}
        def dfs(i, streak):
            if i == n:
                return 1
            if (i, streak) in memo:
                return memo[(i, streak)]
            
            same = 0
            diff = (k - 1) * dfs(i + 1, 1)
            if streak < 2: 
                same = 1 * dfs(i + 1, streak + 1)
            
            memo[(i, streak)] = same + diff
            return memo[(i, streak)]
        return dfs(0, 0)
        