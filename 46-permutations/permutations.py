class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = [] 

        def dfs(current): 
            if len(current) == n:
                res.append(current[:])
                return 
            
            for i in range(n):
                if used[i]:
                    continue 
                used[i] = True
                current.append(nums[i])
                dfs(current)
                used[i] = False 
                current.pop()
        dfs([])
        return res

            

        