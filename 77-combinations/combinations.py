class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        goal: return all possible combinations of length k by choosing numbers between [1, n]

        approach: 
        - backtracking 
        '''
        res = []
        def dfs(i, curr):
            if len(curr) == k: 
                res.append(curr[:])
                return 
            
            for j in range(i, n + 1):
                curr.append(j)
                dfs(j + 1, curr)
                curr.pop()
        dfs(1, [])
        return res

        