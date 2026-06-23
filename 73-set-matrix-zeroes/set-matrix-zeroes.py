class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        shouldZeroFirstRow, shouldZeroFirstColumn = False, False
        for i in range(n):
            if matrix[0][i] == 0:
                shouldZeroFirstRow = True 
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                shouldZeroFirstColumn = True
                break 
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n): 
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if shouldZeroFirstRow:
            for i in range(n):
                matrix[0][i] = 0
        
        if shouldZeroFirstColumn:
            for i in range(m):
                matrix[i][0] = 0
     
        