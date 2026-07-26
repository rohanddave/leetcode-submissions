class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        '''
        problem:
        - square board 
        - starting at bottom right and ending at top right 
        - X is an obstacle 
        - 1,2...,9 numeric characters 
        - move up, left, or up left in one monve 

        goal: return [maximum sum of numeric characters collectable, number path with max sum]. return [0, 0] if not path 

        observation: 
        - number are single digit positive numbers 
        - cannot move into an obstacle 
        - move from bottom right to top left 
        
        example: 
        Input: board = [E 1 2,
                        1 X 1,
                        2 1 S ]
        Output: [4,2]

        approach:
        - 
        '''

        MOD = 10**9 + 7 
        m = len(board)
        memo = {}
        def dfs(r, c): 
            if r == m - 1 and c == m - 1: 
                return 0, 1
            if (r, c) in memo:
                return memo[(r, c)]
            
            curr = int(board[r][c] if board[r][c] != 'E' else 0)
            right = (float('-inf'), 0)
            bottom = (float('-inf'), 0)
            bottom_right = (float('-inf'), 0)

            if c + 1 < m and board[r][c + 1] != 'X':
                right = dfs(r, c + 1)
            if r + 1 < m and board[r + 1][c] != 'X':
                bottom = dfs(r + 1, c)
            if r + 1 < m and c + 1 < m and board[r + 1][c + 1] != 'X':
                bottom_right = dfs(r + 1, c + 1)
            
            max_nei_value = max(right[0], bottom[0], bottom_right[0])
            ways = 0
            if right[0] == max_nei_value:
                ways += right[1] 
            if bottom[0] == max_nei_value: 
                ways += bottom[1]
            if bottom_right[0] == max_nei_value: 
                ways += bottom_right[1] 

            memo[(r, c)] = curr + max_nei_value, ways % MOD
            return memo[(r, c)]
        
        max_value, ways = dfs(0, 0)
        if max_value == float('-inf'):
            return [0, 0]
        return [max_value, ways]
        


        