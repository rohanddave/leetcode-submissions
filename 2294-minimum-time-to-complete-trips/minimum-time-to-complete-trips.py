class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        problem: 
        - time[i] = time taken by ith bus to complete 1 trip 
        
        goal: return min itme required for all buses to complete atleast totalTrips 

        observations: 
        - time[i] * totalTrips = time taken by ith bus to complete totalTrips 
        - search space is between [1, max(time) * totalTrips]
        - search space is monotonic F F F T T T T T
        - we want to find the first index where True
        '''

        def can(x): 
            count = 0
            for t in time: 
                count += x // t
            return count >= totalTrips

        l, r = 1, max(time) * totalTrips

        while l < r: 
            m = (l + r) // 2 
            if can(m): 
                r = m 
            else: 
                l = m + 1
        return l

        