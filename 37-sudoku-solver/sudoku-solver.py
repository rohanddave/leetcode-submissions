class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        grid = [[set() for _ in range(n // 3)] for _ in range(n // 3)]

        empty = []

        for i in range(m): 
            for j in range(n):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    grid[i//3][j//3].add(int(board[i][j]))

        def dfs(i):
            if i == len(empty):
                return True
            
            r, c = empty[i]

            for candidate in range(1, 10):
                if (
                    candidate in rows[r] or
                    candidate in cols[c] or 
                    candidate in grid[r // 3][c // 3]
                ): 
                    continue
                board[r][c] = str(candidate)
                rows[r].add(candidate)
                cols[c].add(candidate)
                grid[r//3][c//3].add(candidate)
                if dfs(i + 1):
                    return True
                board[r][c] = '.'
                rows[r].remove(candidate)
                cols[c].remove(candidate)
                grid[r//3][c//3].remove(candidate)
            return False
        
        dfs(0)
            


        