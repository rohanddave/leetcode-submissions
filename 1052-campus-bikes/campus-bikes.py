class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        '''
        problem: 
        - campus on a 2d plane 
        - n = workers
        - m = bikes 
        - wokers <= bikes
        - workers[i] = [x, y] x-y co ordinate of ith worker
        - bikes[j] = [x, y] x-y co ordinate of jth bike 
        - all positions are unique 
        - assign closest bike (manhattan distance) to each worker;  tie breaker = smallest worker index and smallest bike index
        
        goal: return answer array where answer[i] = index of bike ith worker is assigned to

        example: 

        observations: 
        - points are unique so no bike or worker overlap
        - two different workers contend for the same bike (same min distance), in that case we assign to the worker with smaller index. this can be done by scannign the worker list left to right (but this might not work since we would have to recompute the distances of available bikes for each worker)
        - a worker has multiple bikes at the same min distance, assign the bike with the lower index (can be done with using the bike index as the second key in the min heap)
        - it is always possible to assign a bike to a worker since number of bikes >= number of workers. 

        approach: 
        - for each worker scanning from left to right (for the tie breaker of smaller worker index getting priority)
            - for each unassigned bike compute distance and populate min heap 
            - assign the smallest dist bike
        bottleneck here is recomputing the distance to available bikes. should we explore a optimization?
        '''
        buckets = [[] for _ in range(2001)]
        n, m = len(workers), len(bikes)
        for worker_idx in range(n):
            for bike_idx in range(m):
                worker_x , worker_y = workers[worker_idx]
                bike_x, bike_y = bikes[bike_idx]
                distance = abs(worker_x - bike_x) + abs(bike_y - worker_y)
                buckets[distance].append((distance, worker_idx, bike_idx))
        
        answer = [-1] * n
        used_bikes = set()
        for bucket in buckets: 
            if len(bucket) == 0:
                continue 
            for _, worker_idx, bike_idx in bucket: 
                if bike_idx in used_bikes or answer[worker_idx] != -1:
                    continue
                answer[worker_idx] = bike_idx
                used_bikes.add(bike_idx)
        return answer

        