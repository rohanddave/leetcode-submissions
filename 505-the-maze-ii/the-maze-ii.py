class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        heap = [(0, start[0], start[1])] # (cost, r, c)
        best = {(start[0], start[1]): 0}

        while heap: 
            dist, r, c = heapq.heappop(heap)

            if r == destination[0] and c == destination[1]: 
                return dist 
            
            if dist > best[(r, c)]:
                continue 

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r, c 
                roll_dist = 0
                while 0 <= nr < m and 0 <= nc < n and maze[nr][nc] != 1: 
                    nr += dr
                    nc += dc 
                    roll_dist += 1
                nr -= dr
                nc -= dc 
                roll_dist -= 1
                nei_dist = dist + roll_dist 
                if nei_dist < best.get((nr, nc), float('inf')):
                    heapq.heappush(heap, (nei_dist, nr, nc))
                    best[(nr, nc)] = nei_dist
        return -1
