class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        '''
        goal: return minimum possible maximum working time of any assignment 

        inputs:
        jobs[i] = amount of time to complete ith job 
        k = number of workers 

        constraints: 
        - each job assigned to exactly one worker 
        - working time of worker = sum of completion time of all jobs

        observations: 
        - answer is in the search space [max(jobs), sum(jobs)]
        - the search space is monotonic
        - can(load) return true if all jobs can be completed with each k having at most load 

        how do we write the can(load) function? 
        need to create k subsets with 0 <= sum <= load
        '''
        def can(load):
            nonlocal k  
            workers = [0] * k 

            def dfs(i): 
                if i == len(jobs):
                    return True
                
                for j in range(len(workers)): 
                    if workers[j] + jobs[i] > load:
                        continue
                    workers[j] += jobs[i]
                    if dfs(i + 1):
                        return True 
                    # backtrack 
                    workers[j] -= jobs[i]
                    if workers[j] == 0:
                        break
                return False
            return dfs(0)

        left, right = max(jobs), sum(jobs)

        while left < right: 
            m = (left + right) // 2

            if can(m):
                right = m
            else:
                left = m + 1
        return left
        