class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        mapping = {} 
        for i in range(m): 
            for j in range(n): 
                mapping[mat[i][j]] = (i, j)
            
        rows = [0] * m
        cols = [0] * n

        for i in range(len(arr)):
            row, col = mapping[arr[i]]
            rows[row] += 1
            cols[col] += 1
            if rows[row] == n or cols[col] == m:
                return i
                 

        