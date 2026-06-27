class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()

        for r in range(m):
            for c in range(n): 
                if rooms[r][c] == 0:
                    q.append((0, r, c))

        while q: 
            dist, r, c = q.popleft() 

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
                    q.append((dist + 1, nr, nc))
                    rooms[nr][nc] = dist + 1
        
