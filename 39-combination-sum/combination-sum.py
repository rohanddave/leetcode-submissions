class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [] 
        def dfs(start, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return 
            if start == len(candidates) or candidates[start] + curr_sum > target:
                return 
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(i, curr, curr_sum + candidates[i])
                curr.pop()
        
        dfs(0, [], 0)
        return res


        