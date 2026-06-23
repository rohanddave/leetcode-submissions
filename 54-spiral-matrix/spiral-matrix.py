class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n - 1, 0, m - 1
        res = []

        while l <= r and t <= b: 
            # left to right
            for i in range(l, r + 1): 
                res.append(matrix[t][i])
            t += 1

            if t > b:
                break
            
            # top to bottom
            for j in range(t, b + 1): 
                res.append(matrix[j][r])
            r -= 1

            if l > r: 
                break

            # right to left 
            for i in range(r, l - 1, -1): 
                res.append(matrix[b][i])
            b -= 1

            if t > b:
                break
            
            # bottom to top
            for j in range(b, t - 1, -1): 
                res.append(matrix[j][l])
            l += 1
        return res

        