import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        '''
        input:
        hour = amt of time to reach office 
        n = number of trains to take in sequential order 
        dist[i] = distance for ith train ride 

        each train can depart at an integer hour so might need to wait
        example: if a ride takes 1.5 hours must wait 0.5 hours to get on the next train 

        goal: minimum positive integer that all trains must travel to reach office on time, -1 if impossible

        observations: 
        - total distance to be travelled to reach office = sum(dist) 
        - time taken by each train i = travel time + wait time = ceil(dist[i]/speed)
        - answer lies in the space [1, ceil(sum(dist)/hour)]
        - answer space is monotonic: F F F T T T because once a speed guarantees reaching in time anything faster will also guarantee reaching in time
        
        Example: 
        Input: dist = [1,3,2], hour = 2.7
        Output: 3

        speed = dist / time 
        total distance = 6

        approach: 
        - perform binary search on speed where range is [1, inf]
        - can(speed) checks 
        '''
        def can(speed): 
            n = len(dist)
            time = 0
            for i in range(n): 
                if i == n - 1: 
                    time += dist[i]/speed
                else: 
                    time += math.ceil(dist[i]/speed)
            return time <= hour
        
        if len(dist) - 1 >= hour:
            return -1
        
        left, right = 1, 10**7
        while left < right: 
            m = (left + right) // 2
            if can(m):
                right = m
            else:
                left = m + 1
        return left 
