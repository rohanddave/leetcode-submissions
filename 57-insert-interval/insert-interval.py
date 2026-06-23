class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def does_overlap(a, b): 
            return not (a[1] < b[0] or a[0] > b[1])
        
        intervals.sort() 
        res = [] 
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and does_overlap(intervals[i], newInterval): 
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        
        res.append(newInterval) 

        while i < len(intervals): 
            res.append(intervals[i])
            i += 1
        
        return res