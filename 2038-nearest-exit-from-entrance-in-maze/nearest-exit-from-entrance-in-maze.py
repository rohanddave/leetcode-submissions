class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        goal: return min dist from entrance to nearest exit; -1 if no path

        approach: 
        - perform a bfs from start 
        - explore only empty cells 
        - the first one to reach a cell that is at the boundry is the nearest exit 
        - return -1 if not 
        '''
        m, n = len(maze), len(maze[0])
        start = (entrance[0], entrance[1])
        q = collections.deque([(0, entrance[0], entrance[1])])
        visited = {start}

        while q: 
            dist, row, col = q.popleft() 

            if ((row, col) != start) and (row == m - 1 or row == 0 or col == 0 or col == n - 1):
                return dist
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc 
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    q.append((dist + 1, nr, nc))
                    visited.add((nr, nc))
        return -1
        