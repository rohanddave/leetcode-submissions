class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        '''
        goal: return a 1 indexed array costs of length n where costs[i] is the min cost to reaech stop i from stop 0 

        observations: 
        - a prefix DP does not work since we want the min cost to reach each stop 
        - a suffix DP instead works i.e. dfs(i, is_regular) returns the min cost to reach stop i = [0: i] instead of a prefix definition of [i:n]
        '''
        n = len(express) 
        memo = {} 
        def dfs(i, is_regular): 
            if i < 0:
                return 0 if is_regular else expressCost
            if (i, is_regular) in memo: 
                return memo[(i, is_regular)]
            
            curr_cost = regular[i] if is_regular else express[i]
            
            stay = curr_cost + dfs(i - 1, is_regular) 
            change = curr_cost + (0 if is_regular else expressCost) + dfs(i - 1, not is_regular)
            memo[(i, is_regular)] = min(stay, change)
            return memo[(i, is_regular)]
        answer = [0] * n
        for i in range(n): 
            answer[i] = min(dfs(i, True), dfs(i, False))
        return answer
        