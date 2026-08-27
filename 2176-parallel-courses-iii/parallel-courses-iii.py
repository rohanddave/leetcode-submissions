class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = collections.defaultdict(list) 

        for prereq, course in relations: 
            adj[course].append(prereq)
        @cache
        def dfs(course): 
            max_prereq_time = 0 
            for prereq in adj[course]: 
                max_prereq_time = max(max_prereq_time, dfs(prereq))
            return max_prereq_time + time[course - 1]
        return max(dfs(course) for course in range(1, n + 1))

        