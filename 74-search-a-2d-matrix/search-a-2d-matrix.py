class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l_row, r_row = 0, m - 1
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2

            if matrix[m_row][0] <= target <= matrix[m_row][n - 1]: 
                l, r = 0, n - 1
                while l <= r: 
                    m = (l + r) // 2
                    if target == matrix[m_row][m]:
                        return True
                    elif target < matrix[m_row][m]:
                        r = m - 1
                    else: 
                        l = m + 1
                return False 
            elif target < matrix[m_row][0]: 
                r_row = m_row - 1
            else: 
                l_row = m_row + 1
        return False

        