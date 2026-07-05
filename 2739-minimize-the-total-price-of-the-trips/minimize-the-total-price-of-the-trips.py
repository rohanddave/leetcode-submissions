class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        '''
        goal: return minimum total price sum to perform all trips

        input:
        - 0 to n - 1 nodes 
        - edges[i] = [a, b] indicates undirected edge between a and b 
        - price[i] = price of ith node
        - price sum of a path = sum of prices of all nodes on the path 
        - trips[i] = [start, end] 
        - before first trip can choose non adjacent nodes and halve the price **** 

        observations: 
        - since it's a tree there is only one path from source to destination
        - does the root of the tree matter? 

        example: 
        [0,1,3]

        approach: 
        - traverse trip path from source to destination using dfs(node, parent, path) starting from start and ending at end while accumulating the path
        - when path found update frequency map of nodes in path to count how many times a node occurs across all paths 
        - then do a tree DP on the tree consisting of all paths (what it is a forest of multiple trees?), where for each node you decide to halve or not
            - can halve only if parent wasn't halved 
            - skip 
        '''
        adj = collections.defaultdict(list) 

        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        freq = collections.defaultdict(int) 

        def trip(start, end):
            def dfs(node, parent, path): 
                path.append(node)
                if node == end: 
                    for path_node in path: 
                        freq[path_node] += 1
                else:
                    for nei in adj[node]:
                        if nei == parent: 
                            continue 
                        dfs(nei, node, path)
                path.pop()
            dfs(start, None, [])
                    
        for start, end in trips: 
            trip(start, end)
        
        def dfs(node, parent): 
            pick = (price[node] // 2 * freq[node])
            skip = (price[node] * freq[node])
            for nei in adj[node]:
                if nei == parent:
                    continue
                child_skip, child_pick = dfs(nei, node)
                pick += child_skip
                skip += min(child_skip, child_pick)
            return skip, pick
        
        pick, skip = dfs(0, -1)
        return min(pick, skip)

        