class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        '''
        problem: 
        - edges of undirected tree 
        - nodes are 0 to n - 1
        - colors[i] represents the color of the ith node 

        goal: return index of ANY root that: 
        - has at most 2 children
        - all nodes at same depth have same color. levels following the pattern (RBW, BWR, WRB). 
        
        return -1 if none exist.

        observations: 
        - r -> b -> w -> r

        approach: 
        - 
        '''
        n = len(colors)
        adj = collections.defaultdict(list)
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
        
        color_order = {'R': 'B', 'B': 'W', 'W': 'R'}
        
        def bfs(node): 
            target_color = colors[node]
            q = collections.deque([node])
            visited = {node}

            while q: 
                level_size = len(q) 
                # print(f'level_size: {level_size} \t target_color: {target_color}')

                for _ in range(level_size): 
                    node = q.popleft()
                    node_color = colors[node]
                    if node_color != target_color:
                        # print(f'returning false for node: {node} with color {node_color}')
                        return False
                    for child in adj[node]:
                        if child == node or child in visited:
                            continue
                        q.append(child)
                        visited.add(child)
                target_color = color_order[target_color]

            return True
        
        for node in range(n):
            if len(adj[node]) <= 2: 
                if bfs(node):
                    return node
        return -1

        