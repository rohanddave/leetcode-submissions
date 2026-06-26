class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        goal: list of ancestors of each node 

        brute force: 
        create a parent map adj list {node: [parent1, parent2]}
        for each node dfs through parents and append each to ancestor list 

        optimization: 
        for u, v if u is the parent of v then all the ancestors of u are also ancestors of v 
        so we don't need to perform the entire dfs from each node we could reuse computations 
        we can leverage top sort because when we process a node all it's ancestors are resolved
        when we resolve 3 how do we know what it's ancestors are? we need a parent list 
        when a node is being resolve: 
        - look at it's parent list add each parent and all it's ancestors 
        sort the ancestor list in the end 
        '''

        parent_map = collections.defaultdict(list) 
        adj = collections.defaultdict(list)
        in_degree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            parent_map[b].append(a)
            in_degree[b] += 1
        
        q = collections.deque()

        for node in range(n):
            if in_degree[node] == 0:
                q.append(node)
        
        ancestors = [set() for _ in range(n)]

        while q: 
            node = q.popleft() 

            for parent in parent_map[node]:
                ancestors[node].add(parent)
                ancestors[node].update(ancestors[parent])

            for nei in adj[node]: 
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return [sorted(s) for s in ancestors]
        