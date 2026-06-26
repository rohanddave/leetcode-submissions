class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        q = collections.deque([(start[0], start[1])])
        visited = {(start[0], start[1])}

        while q: 
            r, c = q.popleft() 

            if r == destination[0] and c == destination[1]:
                return True 

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                start_r, start_c = r, c
                while 0 <= start_r < m and 0 <= start_c < n and maze[start_r][start_c] != 1:
                    start_r, start_c = start_r + dr, start_c + dc
                nr, nc = start_r - dr, start_c - dc 
                if (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        return False


