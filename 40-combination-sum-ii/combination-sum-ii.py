class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, current, target): 
            if target == 0:
                res.append(current[:])
                return 
            if start == len(candidates):
                return 
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break 
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                current.append(candidates[i])
                dfs(i + 1, current, target - candidates[i])
                current.pop()
        
        dfs(0, [], target)
        return res