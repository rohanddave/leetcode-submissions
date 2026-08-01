class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        '''
        problem: 
        - directed graph 
        - source and destination 
        - there exists atleast one path from source to destination 
        - destination has no outgoing edges 
        - graph may have self loops and parallel edges
        
        goal: return true if all paths starting from source ends at destination 

        observation: 
        - if there is a cycle anywhere in path from source then return False 
        - it is also possible that there isn't a cycle and all paths don't end in destination
        '''
        UNVISITED, VISITING, VISITED = -1, 0, 1
        state = collections.defaultdict(lambda: -1)
        adj = collections.defaultdict(list)

        for a, b in edges: 
            adj[a].append(b)
        
        memo = {}
        
        def dfs(node): 
            if state[node] == VISITING:
                return False
            if node in memo:
                return memo[node]
            
            state[node] = VISITING
            ans = node == destination

            for nei in adj[node]: 
                nei_path = dfs(nei)
                ans = ans or nei_path
                if not nei_path:
                    return False
                
            state[node] = VISITED
            memo[node] = ans            
            return memo[node]
        
        return dfs(source)
