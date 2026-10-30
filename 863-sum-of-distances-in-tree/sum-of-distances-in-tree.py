class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        subtree = [1] * n
        answer = [0] * n

        def dfs_bottom_up(node, parent): 
            res = 0

            for child in adj[node]:
                if child == parent:
                    continue
                dfs_bottom_up(child, node)
                subtree[node] += subtree[child]
                answer[node] += answer[child] + subtree[child]
            
        
        def dfs_top_down(node, parent): 

            for child in adj[node]:
                if child == parent:
                    continue 
                
                answer[child] = (
                    answer[node] -
                    subtree[child] + 
                    (n - subtree[child])
                )
                
                dfs_top_down(child, node)
                
        dfs_bottom_up(0, -1) # treat 0 as root of tree 
        dfs_top_down(0, -1) # treat 0 as root of tree 

        return answer
        
        

        
        