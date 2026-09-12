class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = collections.defaultdict(list) 
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)

        bob_path = None
        def dfs_bob(node, parent, path):
            nonlocal bob_path
            path.append(node)
            if node == bob:
                bob_path = path[:]
                return 
            
            for nei in adj[node]: 
                if nei != parent:
                    dfs_bob(nei, node, path)
            path.pop()
        dfs_bob(0, -1, [])

        bob_reach_time = collections.defaultdict(lambda: float('inf'))

        for time, node in enumerate(reversed(bob_path)):
            bob_reach_time[node] = time

        def dfs_alice(node, parent, time):
            curr_cost = amount[node]
            if bob_reach_time[node] < time: 
                curr_cost = 0
            elif bob_reach_time[node] == time: 
                curr_cost = amount[node] // 2
            
            best_nei_cost = float('-inf')
            for nei in adj[node]:
                if nei != parent: 
                    nei_cost = dfs_alice(nei, node, time + 1)
                    best_nei_cost = max(best_nei_cost, nei_cost)
            
            if best_nei_cost == float('-inf'):
                return curr_cost
            return curr_cost + best_nei_cost
        
        return dfs_alice(0, -1, 0)