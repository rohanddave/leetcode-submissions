class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        '''
        combined = (quality, wage, quality/wage)
        Example 1:
        quality = [10,20,5], wage = [70,50,30], k = 2
        quality / wage = quality per dollar
        combined = [(10, 70, 0.142), (20, 50, 0.4), (5, 30, 0.167)]

        Example 2: 
        quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
        combined = [(3,4,0.75), (1,8,0.125), (10,2,5), (10,2,5), (1,7,0.142)]

        approach:
        - sort in ascending order of quality / wage 
        - a worker in the group is the base worker 
        '''
        n = len(quality)
        combined = [(wage[i]/quality[i], quality[i]) for i in range(n)]
        combined.sort() 

        heap = [] 
        res = float('inf')
        quality_sum = 0
        for ratio, q in combined: 
            heapq.heappush(heap, -q)
            quality_sum += q

            if len(heap) > k:
                popped_quality = -1 * heapq.heappop(heap)
                quality_sum -= popped_quality
            if len(heap) == k: 
                res = min(res, ratio * quality_sum)
        return res

