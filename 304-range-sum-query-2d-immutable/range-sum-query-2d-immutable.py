class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        where (r, c) is the bottom right corner of rectangle

        res = prefix[row2][col2] - above - left + above_left
        '''
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n): 
                left = 0 if (j - 1) < 0 else self.prefix[i][j - 1]
                above = 0 if (i - 1) < 0 else self.prefix[i - 1][j]
                diag = 0 if (i - 1) < 0 or (j - 1) < 0 else self.prefix[i - 1][j - 1]
                self.prefix[i][j] = matrix[i][j] + above + left - diag
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        above = 0 if (row1 - 1) < 0 else self.prefix[row1 - 1][col2]
        left = 0 if (col1 - 1) < 0 else self.prefix[row2][col1 - 1]
        diag_left = 0 if (row1 - 1) < 0 or (col1 - 1) < 0 else self.prefix[row1 - 1][col1 - 1]
        return self.prefix[row2][col2] - above - left + diag_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)2