class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        '''
        
        input: 
        n = number of nodes in graph 
        edges 

        observations: 
        - undirected graph 
        - connected trio = three nodes where edge between every pair
        - degree of connected trio = number of edges where on endpoint is in the trio and other is not
        - connected trio = cycle of 3 nodes
        - edges that count in trio that has one vertex outside of trio

        - there is a connected trio if there exists a w which has u and v in it's adj list

        goal: return minimum degree of a connected trio in graph or -1 if no connected trios

        approach: 
       

        '''
        adj = collections.defaultdict(set) 
        degree = collections.defaultdict(int)
        for u, v in edges: 
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        res = float('inf')
        for u, v in edges: 
            for w in adj[u]:
                if w in adj[v]:
                    trio_degree = degree[u] + degree[v] + degree[w] - 6
                    res = min(res, trio_degree)

        return -1 if res == float('inf') else res