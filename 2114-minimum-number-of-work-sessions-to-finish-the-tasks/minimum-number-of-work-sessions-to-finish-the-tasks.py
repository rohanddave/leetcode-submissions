class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        '''
        for each item we need to assign to a session 
        each session can have atmost sessionTime sum


        '''
        n = len(tasks)
        initial_mask = 0
        target_mask = (1 << n) - 1
        memo = {}
        def dfs(mask, remaining_capacity): 
            if mask == target_mask:
                return 0 
            if (mask, remaining_capacity) in memo:
                return memo[(mask, remaining_capacity)]
            
            res = float('inf')
            for i in range(n):
                is_used = (mask >> i) & 1
                if not is_used:
                    new_mask = mask | (1 << i)
                    if tasks[i] <= remaining_capacity: 
                        res = min(res, dfs(new_mask, remaining_capacity - tasks[i]))
                    else: 
                        res = min(res, 1 + dfs(new_mask, sessionTime - tasks[i]))
            memo[(mask, remaining_capacity)] = res
            return memo[(mask, remaining_capacity)]
            
        return 1 + dfs(initial_mask, sessionTime)


        