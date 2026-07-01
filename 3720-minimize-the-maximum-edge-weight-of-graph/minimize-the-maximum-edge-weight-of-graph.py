class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        '''
        goal: return min value of max edge weight after removing edges. if impossible return -1

        remove 0 or more edges under these conditions: 
        - node 0 must be reachable from all other nodes
        - max edge weight is minimized
        - each node has at most threshold outgoing edges 

        observations: 
        - we need to remove edges from node n where out going from n > threshold and try removing the max weighted edge first, make that change only if node 0 is still reachable from this node
        
        example 3:
        threshold = 1
        outgoing = {1: 3, 2: 1, 3: 1, 4: 1, 0: 0}
        nodes with outgoing > threshold = [1]
        candidate edges to be removed = [(1,4,5), (1,3,3), (1,2,1)] => we need to remove 2 edges here 
        if we remove (1,4,5) => possible because node 0 is still reachable through 2, 3
        if we remove (1,3,3) => possible because node 0 is still reachable through 2

        observation: 
        - if we reverse edges and start traversing from 0, if we can reach all nodes then it is a feasible solution 

        approach:
        - to find the min max edge weight we use bin search on answer
        - can(weight) function returns true or false if all nodes are reachable from 0 taking edges that have weight <= weight        
        '''
        adj = collections.defaultdict(list) 
        for u, v, w in edges: 
            adj[v].append((u, w))
        
        def can(weight): 
            visited = set() 
            def dfs(node): 
                visited.add(node)
                for nei, nei_weight in adj[node]:
                    if nei not in visited and nei_weight <= weight:
                        dfs(nei)
            dfs(0)
            return len(visited) == n
        
        if n == 1:
            return 0 
        if threshold == 0:
            return -1 
        if not edges:
            return -1
        left, right = 0, max(weight for _, _, weight in edges)
        while left < right: 
            weight = (left + right) // 2
            if can(weight):
                right = weight 
            else: 
                left = weight + 1
        return left if can(left) else -1