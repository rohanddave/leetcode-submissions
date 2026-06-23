class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose matrix
        for i in range(n): 
            for j in range(n): 
                if j > i: 
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # reverse matrix
        for i in range(n):
            for j in range(n // 2): 
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
