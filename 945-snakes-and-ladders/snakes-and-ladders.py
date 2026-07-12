class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''
        problem: 
        - n x n board 
        - cells are label 1 - n^2 in zig zag manner 
        - starting from board[n - 1][0]
        - next(curr) = [curr + 1, min(curr + 6), n^2)]
        - if next snake or ladder go to destination of snake or ladder 
        - game ends at n^2
        - board[r][c] != -1 then it is a snake or ladder with the value as the destination 
        - take only one snake or ladder per role i.e. if a snake or ladder destination is another snake or ladder do not take the subsequenet one 
        
        goal: return leasst number of dice rolls required to reach n^2, -1 if not possible

        observation: 
        - do we really care if it is a grid?? no because you can only move forward unless you encounter a snake. but we need to know the position in the grid because we need to know if it is a snake, ladder or empty cell
        - can we get the r,c from just the cell value? ceil(value/6) + n 
        - cycles are possible so dynamic programming is not possible 
        - since we want minimum number of rolls we can use a bfs approach 

        approach: 
        - bfs
        - q stores (rolls, val)
        - visited stores (val)
        - at cell curr
            - try all possible next candidates: [curr + 1, min(curr + 6), n^2)]
        '''
        n = len(board)
        def get_r_c(val):
            val -= 1
            row_from_bottom = val // n
            row = n - row_from_bottom - 1
            rem = val % n
            # if on even row
            if row_from_bottom % 2 == 0:
                col = rem
                return row, col
            else:
                col = n - 1 - rem
                return row, col
        
        q = collections.deque([(0, 1)])
        visited = {1}
        target = n ** 2

        while q: 
            rolls, curr = q.popleft() 

            if curr == target:
                return rolls 

            for nei in range(curr + 1, min(curr + 6, target) + 1):
                r, c = get_r_c(nei)
                destination = nei if board[r][c] == -1 else board[r][c]
                if destination not in visited:
                    q.append((rolls + 1, destination))
                    visited.add(destination)
        return -1

        
