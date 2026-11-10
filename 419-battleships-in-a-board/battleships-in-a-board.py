class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m, n = len(board), len(board[0])
        count = 0
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'X':
                    count += 1
                    q = collections.deque([(row, col)])
                    while q: 
                        r, c = q.popleft()

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc 
                            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'X':
                                q.append((nr, nc))
                                board[nr][nc] = '.'
        return count