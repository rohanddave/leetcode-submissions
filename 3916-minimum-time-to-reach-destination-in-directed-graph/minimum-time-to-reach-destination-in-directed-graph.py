class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # may not need this sorting step because the heap will endforce the sorting structure anyway. when at a current node you take all the edges at the earliest time available
        # edges.sort(lambda x: x[2]) # sort edges by start time

        # create adj list; for each node edges will be in sorted order of start time
        adj = collections.defaultdict(list) 
        for u, v, start, end in edges: 
            adj[u].append((v, start, end))
        
        heap = [(0, 0)] # (curr_time, curr_node)
        min_time = [float('inf')] * n
        min_time[0] = 0

        while heap: 
            time, node = heapq.heappop(heap)

            if node == n - 1: 
                return time 
            
            if time > min_time[node]:
                continue
            
            for nei_node, start, end in adj[node]:
                # cannot take this edge
                if time > end: 
                    continue
                
                new_time = max(time, start) + 1
                if new_time < min_time[nei_node]:
                    heapq.heappush(heap, (new_time, nei_node))
                    min_time[nei_node] = new_time
        return -1

        

        