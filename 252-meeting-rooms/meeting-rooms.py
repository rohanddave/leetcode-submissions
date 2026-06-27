class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def does_overlap(a, b):
            return not (a[1] <= b[0] or a[0] >= b[1])
        intervals.sort() 

        for i in range(len(intervals) - 1): 
            if does_overlap(intervals[i], intervals[i + 1]):
                return False
        return True
