class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        candidate = (-1, -1) # (row idx, count)
        for i in range(m): 
            count = sum(mat[i])
            if count > candidate[1]: 
                candidate = (i, count)
        return candidate

        