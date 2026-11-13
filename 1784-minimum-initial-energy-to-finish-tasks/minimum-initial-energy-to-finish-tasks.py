class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)

        def can(x): 
            curr = x 
            for actual, minimum in tasks: 
                if curr < minimum:
                    return False
                curr = curr - actual
            
            return True

        MAX = sum(actual for actual, minimum in tasks) + max(
            minimum for actual, minimum in tasks
        )
        l, r = 0, MAX 
        while l < r: 
            m = (l + r) // 2
            if can(m):
                r = m
            else: 
                l = m + 1
            
        return l
        