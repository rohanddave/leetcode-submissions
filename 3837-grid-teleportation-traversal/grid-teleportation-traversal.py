class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        '''
        goal: return min number of moves required to reach bottom right. if not possible -1

        observations: 
        - cost to move to empty cell 1
        - cost to teleport 0 
        - portal would be globally visited because if shortest path finds that portal then no other path should use that

        approach: 
        - use 0/1 bfs 
        - q will store (dist, row, col)
        - visited set will only store (row, col) 
        - visited portal set

        '''
        m, n = len(matrix), len(matrix[0])
        portals = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                if matrix[i][j].isupper():
                    portals[matrix[i][j]].append((i, j))

        q = collections.deque([(0, 0, 0)])
        visited_portals = set()
        min_dist = [[float('inf')] * n for _ in range(m)]
        min_dist[0][0] = 0

        while q: 
            dist, r, c = q.popleft() 

            if r == m - 1 and c == n - 1:
                return dist 
            
            if matrix[r][c].isupper() and matrix[r][c] not in visited_portals: 
                visited_portals.add(matrix[r][c])
                for portal_row, portal_col in portals[matrix[r][c]]:
                    if dist < min_dist[portal_row][portal_col]:
                        q.appendleft((dist, portal_row, portal_col))
                        min_dist[portal_row][portal_col] = dist

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#':
                    if dist + 1 < min_dist[nr][nc]:
                        q.append((dist + 1, nr, nc))
                        min_dist[nr][nc] = dist + 1
                        
        return -1

