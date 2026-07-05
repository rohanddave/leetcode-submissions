class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        '''
        goal: return min total cost to reach (m - 1, n - 1) from (0, 0)

        problem: 
        - normal move: right or down => cost = value of destination cell 
        - teleportation: from (i, j) to (x, y) such that grid[x][y] <= grid[i][j] => cost = 0
        - at most k teleportations

        observations: 
        - directed weighted graph (since the weight p1 -> p2 = p2 and p2 -> p1 = p1)
        - normal move costs and teleportation has no cost
        - use dijkstra instead of 0/1 bfs because the cost for normal move is the value of destination cell 
        - a cell i, j can be reached with different number of teleports and hence should be treated differently
        - finding the cells to teleport to is expensive since we would need to rescan the matrix
        
        approach: 
        - 
        '''
        m, n = len(grid), len(grid[0])
        min_heap = [(0, 0, 0, 0)] # (cost, row, col, teleportations used)
        min_cost = collections.defaultdict(lambda:float('inf')) # (row, col, teleportations)
        min_cost[(0, 0, 0)] = 0

        ptr = [0] * (k + 1)
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        
        cells.sort()


        while min_heap: 
            cost, row, col, teleportations_used = heapq.heappop(min_heap)
            
            if row == m - 1 and col == n - 1: 
                return cost 
            
            if cost > min_cost[(row, col, teleportations_used)]: 
                continue
            
            neighbors = set() # (row, col, cost, nei)
            if (row + 1) < m:
                neighbors.add((row + 1, col, cost + grid[row + 1][col], teleportations_used))
            if col + 1 < n:
                neighbors.add((row, col + 1, cost + grid[row][col + 1], teleportations_used))
            
            if teleportations_used < k:
                while ptr[teleportations_used] < len(cells) and cells[ptr[teleportations_used]][0] <= grid[row][col]:
                    val, i, j = cells[ptr[teleportations_used]]
                    if val <= grid[row][col] and (i, j) != (row, col):
                        neighbors.add((i, j, cost, teleportations_used + 1))
                    ptr[teleportations_used] += 1
                
            for nr, nc, nei_cost, nei_teleportations in neighbors: 
                if nei_cost < min_cost[(nr, nc, nei_teleportations)]:
                    heapq.heappush(min_heap, (nei_cost, nr, nc, nei_teleportations))
                    min_cost[(nr, nc, nei_teleportations)] = nei_cost
            
