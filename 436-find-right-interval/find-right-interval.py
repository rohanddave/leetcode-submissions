class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''
        problem: 
        - right interval = start_j >= end_i 
        - i may equal to j (only when interval is of length 0 i.e. [3, 3])
        
        goal: return array of right intervals for each interval. if no right interval attach - 1

        observations: 
        - an interval maybe it's right interval only when start and end are equal
        - start indices are unique (we should leverage this for a solution)
        - start_i <= end_i
        - 

        brute force: 
        - for each interval look at all other intervals and keep track of the interval with the smallest start that is greater or equal to current end
        - TC: O(n^2), SC: O(1)

        approach: 
        - left to right scan of sorted list in order of: sort(x[1], x[0]) 
        - maintain another list sorted in ascneding order of start time. maintain pointer j for this list 
        - increment j till another_list[j][0] >= list[i][1]
        - if j == len(intervals); ans[i] = -1

        TC: O(n log n + n log n + n + n) since amortized work inside the loop = (n log n)
        SC: O(2n)

        example: 
        Input: intervals = [[1,4],[2,3],[3,4]] => [[2, 3], [1, 4], [3, 4]]
        Output: [-1,2,-1]

        '''
        n = len(intervals)
        
        indexed = [(start, end, idx) for idx, (start, end) in enumerate(intervals)]

        by_start = sorted(indexed)
        j = 0

        by_end = sorted(indexed, key=lambda x: x[1])

        answer = [-1] * n

        for start, end, idx in by_end:
            while j < n and by_start[j][0] < end: 
                j += 1
            
            if j < len(intervals): 
                answer[idx] = by_start[j][2]

        return answer