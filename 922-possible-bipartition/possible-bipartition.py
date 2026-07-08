class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list) 
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        UNCOLORED, WHITE, BLACK = -1, 0, 1
        colors = [UNCOLORED] * (n + 1)

        def bfs(start): 
            nonlocal UNCOLORED, WHITE, BLACK
            q = collections.deque([start]) 
            colors[start] = WHITE

            while q: 
                node = q.popleft() 

                for nei in adj[node]:
                    if colors[nei] == colors[node]:
                        return False 
                    elif colors[nei] == UNCOLORED:
                        colors[nei] = WHITE if colors[node] == BLACK else BLACK
                        q.append(nei)
            return True

        for i in range(1, n + 1):
            if colors[i] == UNCOLORED: 
                if not bfs(i):
                    return False 
        return True
