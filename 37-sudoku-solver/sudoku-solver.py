class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        rows = [0] * m
        cols = [0] * m
        grid = [0] * m

        empty = []

        for i in range(m): 
            for j in range(n):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    mask = (1 << int(board[i][j]))
                    rows[i] |= mask
                    cols[j] |= mask
                    grid[(i // 3) * 3 + (j // 3)] |= mask
        

        def dfs(i):
            if i == len(empty):
                return True
            
            r, c = empty[i]

            for candidate in range(1, 10):
                if (
                    rows[r] & (1 << candidate) or
                    cols[c] & (1 << candidate) or
                    grid[(r // 3) * 3 + (c // 3)] & (1 << candidate)
                ): 
                    continue
                
                
                prev_row, prev_col, prev_grid = rows[r], cols[c], grid[(r // 3) * 3 + (c // 3)]

                mask = (1 << candidate)
                board[r][c] = str(candidate)
                rows[r] |= mask
                cols[c] |= mask
                grid[(r // 3) * 3 + (c // 3)] |= mask

                if dfs(i + 1):
                    return True
                
                # backtrack
                board[r][c] = '.'
                rows[r] = prev_row
                cols[c] = prev_col
                grid[(r // 3) * 3 + (c // 3)] = prev_grid
            return False
        
        dfs(0)
            


        