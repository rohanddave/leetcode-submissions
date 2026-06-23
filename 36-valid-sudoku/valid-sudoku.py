class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for i in range(n)]
        cols = [set() for i in range(n)]
        grid = [[set() for _ in range(n//3)] for i in range(n // 3)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in rows[i] or num in cols[j] or num in grid[i//3][j//3]:
                    return False 
                rows[i].add(num)
                cols[j].add(num)
                grid[i//3][j//3].add(num)
        return True
        