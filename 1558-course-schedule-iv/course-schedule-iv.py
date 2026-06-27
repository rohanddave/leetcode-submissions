class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        goal: return boolean array answer where answer[j] = answer to jth query
        query[j] = [uj, vj] => true if uj is a prereq of vj

        observation: 
        - it is a DAG
        - ui != vi


        approach: 
        1st approach:
        - create a parent map graph
        - starting at v travel all paths and return true if found u

        2nd approach: 
        - top sort and store the immediate pre reqs for each 
        '''
        adj = collections.defaultdict(list) 
        in_degree = [0] * numCourses
        for prereq, course in prerequisites:
            adj[prereq].append(course) 
            in_degree[course] += 1
        
        
        q = collections.deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
        
        res = collections.defaultdict(set)
        while q: 
            course = q.popleft() 

            for nei_course in adj[course]:
                res[nei_course].add(course)
                res[nei_course].update(res[course])

                in_degree[nei_course] -= 1
                if in_degree[nei_course] == 0:
                    q.append(nei_course)
        
        ans = []
        for u, v in queries: 
            ans.append(u in res[v])
        return ans


        