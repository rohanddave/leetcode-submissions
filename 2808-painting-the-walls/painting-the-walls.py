class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        '''
        goal: return min cost to paint n walls 

        problem:
        - exactly two painters: 1 paid and 1 free
        - paid paints wall i in time[i] and cost[i] amount 
        - free paints any wall in 0 cost and 1 unit of time 
        - free painter can only be used when paid is busy

        observations: 
        - walls can be colored in any order not necessarily in order going from 1 - n 
        - if paid painter is assigned ith wall then free painter can paint time[i] walls at 0 cost 
        - that means 1 + time[i] walls are painted in cost[i] 

        approach: 
        - dfs function returns the cost to paint ith wall 
        - 
        '''
        n = len(cost)
        memo = {}
        def dfs(i, painted_count): 
            if painted_count >= n:
                return 0 
            if i >= n:
                return float('inf')
            if (i, painted_count) in memo:
                return memo[(i, painted_count)]
            
            pick = cost[i] + dfs(i + 1, painted_count + 1 + time[i])
            skip = dfs(i + 1, painted_count)
            memo[(i, painted_count)] = min(pick, skip)
            return memo[(i, painted_count)]
        return dfs(0, 0)

        