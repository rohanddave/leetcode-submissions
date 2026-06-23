class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(start, current): 
            res.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                dfs(i + 1, current)
                current.pop()
        dfs(0, [])
        return res



        