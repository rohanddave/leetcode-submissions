class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n 

        nums.sort()
        res = []

        def dfs(curr): 
            if len(curr) == n:
                res.append(curr[:])
                return 

            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if used[i]:
                    continue
                used[i] = True 
                curr.append(nums[i])
                dfs(curr)
                used[i] = False
                curr.pop()
        dfs([])
        return res