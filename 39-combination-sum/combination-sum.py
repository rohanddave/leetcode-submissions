class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
                current.append(candidates[i])
                dfs(i, current, target - candidates[i])
                current.pop()
        
        dfs(0, [], target)
        return res

        