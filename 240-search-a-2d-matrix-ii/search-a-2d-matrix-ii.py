class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while c >= 0  and r < m:
            if matrix [r][c] == target:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False