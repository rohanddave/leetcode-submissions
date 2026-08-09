class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        adj = collections.defaultdict(list) # u: (w, v)
        n = len(distance)

        for i, dist in enumerate(distance):
            source, dest = i, (i + 1) % n 
            adj[source].append((dist, dest))
            adj[dest].append((dist, source))
        
        min_dist = [float('inf')] * n
        min_dist[start] = 0
        heap = [(0, start)] # (dist, node)

        while heap: 
            dist, node = heapq.heappop(heap)

            if dist > min_dist[node]:
                continue
            
            if node == destination: 
                return dist
            
            for nei_dist, nei in adj[node]: 
                if nei_dist + dist < min_dist[nei]: 
                    heapq.heappush(heap, (nei_dist + dist, nei))
                    min_dist[nei] = nei_dist + dist

        return -1

        