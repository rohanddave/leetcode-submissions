class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list) # u: [(v, w)]        
        for u, v in edges: 
            adj[u].append((v, 0))
            adj[v].append((u, 1))
        
        answer = [float('inf')] * n

        def dfs(node, parent): 
            cost = 0
            for nei, nei_cost in adj[node]:
                if nei == parent:
                    continue
                cost += nei_cost + dfs(nei, node)
            return cost
                
        initial_root = 0
        answer[initial_root] = dfs(initial_root, None)
    
        def dfs2(node, parent): 
            for nei, nei_cost in adj[node]: 
                if nei == parent:
                    continue
                answer[nei] = answer[node] + (1 if nei_cost == 0 else -1)
                dfs2(nei, node)

        dfs2(initial_root, None)
        return answer
