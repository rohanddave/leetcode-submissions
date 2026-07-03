class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        goal: return array containing answer to queries 

        observations: 
        - answer[j] = right - left + 1 for the smallest interval such that left <= queries[j] <= right 

        approach: 
        - line sweep 
        - maintain a min heap of intervals by size (size, interval[0], interval[1])
        - sort queries in ascending order
        - sort intervals in ascending order of start time 
        - for each query
            insert into min heap intervals where intervals[i][1] <= query 
            remove from min heap intervals where intervals[i][0] >= query 
            if min_heap:
                answer[j] = min_heap[0][0]
        '''
        # sort intervals in ascending order of start time 
        intervals.sort() 
        i = 0 # interval pointer

        queries = [(query, j) for j, query in enumerate(queries)] # zip queries with indices because sorted will ruin order
        
        answer = [-1] * len(queries) # result

        min_heap = [] 
        for query, j in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, (size, intervals[i][1]))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                answer[j] = min_heap[0][0]
            
        return answer
        