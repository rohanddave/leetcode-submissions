class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        problem: 
        - schedule all jobs over exactly d days (atleast one job one day)
        - difficulty of schedule = sum of difficulties of each day 
        - diffculty of a day = max difficulty of jobs done that day

        goal: return min difficulty of job schedule. -1 if not possible

        observations:
        - can schedule multiple jobs in one day
        - each day could have an unequal number of jobs 
        - how to decide how many jobs in a day? 
        - for min job difficulty take the largest and stack as many larger ones under the same day
        - this looks like a partition DP / backtracking, scan left to right and try to make a d - 1 partitions over the entire array


        approach: 
        - partition DP 
        - scan left to right and try to make d - 1 partitions or d?
        - 
        '''

        n = len(jobDifficulty) 
        if d > n:
            return -1
        
        res = float('inf') # this will store the minimum diffculty 
        schedule_difficulty = 0
        memo = {} 

        def dfs(i, days_left): 
            nonlocal res
            # we reached a valid split; update result
            if i >= n and days_left == 0: 
                return 0
            # reached the end but there are days left - invalid split
            if i >= n or n - i < days_left:
                return float('inf')
            if days_left == 1:
                return max(jobDifficulty[i:])
            if (i, days_left) in memo:
                return memo[(i, days_left)]

            best_schedule = float('inf')
            day_max = float('-inf')
            for j in range(i, n - days_left + 1): 
                # day_difficulty = max(jobDifficulty[i:j])
                day_max = max(day_max, jobDifficulty[j])
                best_schedule = min(best_schedule, day_max + dfs(j + 1, days_left - 1))
            
            memo[(i, days_left)] = best_schedule
            return memo[(i, days_left)]

        return dfs(0, d)

            

        
