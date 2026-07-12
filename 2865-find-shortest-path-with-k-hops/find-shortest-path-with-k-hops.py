class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        '''
        problem: 
        - 0 indexed undirected weighted connected graph
        - n = number of nodes [0, n - 1]
        - edges[i] = [u,v,w] edge from u -> v and v -> u with weight w 
        - s = source node
        - d = destination node
        - k = maximum number of hops 
        - a hop makes an edge weight 0 

        goal: return length of shortest path from s to d with at most k hops (over edges)

        observation: 
        - find min cost path from s to d while making at most k edge cost 0
        - shortest path = min cost from s to d
        - cycles are possible 
        - no repeated edges 
        - no self loops 
        - graph is connected i.e. always possible to reach d from s
        - greedily making edges 0 might not work
        - we need to try using an edge as 0 or not 
        - we can use dynamic programming but cycles are possible ?? 

        example: 
        - (4->0->6->3->2->1) = 9 + 4 + 2 + 4 + 4 = 23
          (4->0->6->3->1) = 9 + 4 + 2 + 9 = 24 

        approach: 
        - generate all paths from source to destination and greedily make k maximum edge costs 0 
        - generating all paths is expensive. should we explore an optimiation?
        - use dijkstra
        - min heap stores (dist, number of hops, node)
        - min dist / visited stores distances for the state (node, number of hops) since reach the same node with different number of hops is a different state 

        '''
        adj = collections.defaultdict(list) 
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        min_dist = collections.defaultdict(lambda:float('inf'))
        min_dist[(s, 0)] = 0 # (node, hops used)
        min_heap = [(0, 0, s)] # (dist, hops, node)

        while min_heap:
            dist, hops, node = heapq.heappop(min_heap)

            if node == d:
                return dist 
            
            # stale entry in heap
            if dist > min_dist[(node, hops)]:
                continue
            
            for nei, nei_weight in adj[node]:
                if dist + nei_weight < min_dist[(nei, hops)]:
                    heapq.heappush(min_heap, (dist + nei_weight, hops, nei))
                    min_dist[(nei, hops)] = dist + nei_weight

                # can use a hop
                if hops < k: 
                    if dist < min_dist[(nei, hops + 1)]:
                        heapq.heappush(min_heap, (dist, hops + 1, nei))
                        min_dist[(nei, hops + 1)] = dist
