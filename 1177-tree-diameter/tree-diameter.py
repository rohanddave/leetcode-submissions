class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        '''
        goal: return the number of edges in the longest path in tree

        observations:
        - not a binary tree 
        - we're returning the number of edges not the number of vertices 
        - longest path need not be from root to node, can be any path 
        - we're not given the root of the tree 
        - number of edges in path = number of vertices in path - 1

        the maximum path length through node N = max(height of subtree) + 1
        - if there is no node => 0
        - if there is just one node => 1
        - if there are two nodes => 2
        a 
        |
        b 

        longest path to chain with parent = 1 + max(height of children)
        update global max as 2 + max height of children + next greatest height of children 

        approach: 
        - start dfs from any node 
        '''
        if not edges:
            return 0
        adj = collections.defaultdict(list) 
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        answer = 0
        def dfs(node, parent): 
            nonlocal answer
            best = 0
            second = 0

            for child in adj[node]: 
                if child == parent: 
                    continue 
                child_height = dfs(child, node)
                if child_height > best:
                    second = best
                    best = child_height
                elif child_height > second:
                    second = child_height
            
            answer = max(answer, 1 + best + second)
            return 1 + best
        
        dfs(edges[0][0], -1)
        return answer - 1

            
