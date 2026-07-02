class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        '''
        goal: return maximum safeness factor of all paths from 0,0 to n - 1, n - 1

        safeness factor of a path = min manhattan distance from any cell to any theif in grid

        manhattan(p1, p2) = |p1[0] - p2[0]| + |p1[1] - p2[1]|

        example:
        grid = [
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 0]
        ]
        manhattan =[
            [2, 1, 0],
            [3, 2, 1],
            [4, 3, 2]
        ]

        approach: 
        - use flood fill to create & store the safeness for each cell 
        - use backtracking to generate all paths from 0, 0 to n - 1, n - 1 and track the min safeness value seen in the path 
        - when reached the end update global max with current path safeness value

        optimization: 
        - instead of tracking all paths use dijkstra using a max heap
        '''
        n = len(grid)
        # flood fill 
        safeness = [[-1] * n for _ in range(n)]
        q = collections.deque() 

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((0, i, j))
                    safeness[i][j] = 0
        
        while q: 
            dist, r, c = q.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safeness[nr][nc] == -1:
                    q.append((dist + 1, nr, nc))
                    safeness[nr][nc] = dist + 1
        
        # dijkstra
        max_heap = [(-safeness[0][0], 0, 0)] 
        visited = {(0, 0)}

        while max_heap: 
            safe, r, c = heapq.heappop(max_heap)
            safe = -1 * safe

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_safe = min(safe, safeness[nr][nc])
                    heapq.heappush(max_heap, (-new_safe, nr, nc))
                    visited.add((nr, nc))

        