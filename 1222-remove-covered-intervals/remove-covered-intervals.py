class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
        problem: 
        - intervals[i] represents [l, r)
        
        goal: remove the number of covered intervals

        observation: 
        - intervals are in any order 
        - combining two intervals does not make the third interval covered
        
        approach: 
        - if we sort by the start and end: [[1,4], [1, 8], [2, 5], []]
        
        [15, 16], [2, 8]
        --------------
            -------------
               ---------
        '''
        intervals.sort(key=lambda x: (x[0], -x[1])) 
        res = [intervals[0]]

        def fully_covered(a, b): 
            return a[0] <= b[0] and a[1] >= b[1]

        for i in range(1, len(intervals)): 
            if not fully_covered(res[-1], intervals[i]):
                res.append(intervals[i])
        
        return len(res)
        