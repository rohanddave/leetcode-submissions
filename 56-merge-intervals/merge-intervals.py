class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        def does_overlap(a, b): 
            return not (a[1] < b[0] or a[0] > b[1])
        
        res = [intervals[0]]
        for i in range(1, len(intervals)): 
            if does_overlap(res[-1], intervals[i]):
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else: 
                res.append(intervals[i])
        return res

        