class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        '''
        goal: minimum cost of path from any col in the first row to any col in last row

        problem: 
        - distinct integers [0, m * n - 1]
        - can only move from any col in row to any col in row + 1
        - moveCost[i][j] = cost of moving from cell with value i to cell in col j of next row

        observation: 
        - path cost = sum of all values of visited cells + sum of cost of all moves made
        - once we've travelled from row -> row + 1 we never need to look at row

        approach: 
        - at current row try all possible moves to row + 1
        - dfs function returns the minimum cost from row, col 
        - 
        '''
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(row, col):
            if row == m - 1:
                return grid[row][col]
            if (row, col) in memo:
                return memo[(row, col)]

            cost = float('inf')

            curr_val = grid[row][col]

            for nei_col in range(n):
                nei_move_cost = moveCost[curr_val][nei_col]
                total_nei_cost = curr_val + nei_move_cost + dfs(row + 1, nei_col)
                cost = min(cost, total_nei_cost)
            memo[(row, col)] = cost
            return memo[(row, col)]
        return min(dfs(0, col) for col in range(n))

