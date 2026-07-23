class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # row_prefix[r][c] = sum of grid[r][0:c]
        row_prefix = [[0] * (n + 1) for _ in range(m)]

        # col_prefix[c][r] = sum of grid[0:r][c]
        col_prefix = [[0] * (m + 1) for _ in range(n)]

        for r in range(m):
            for c in range(n):
                row_prefix[r][c + 1] = row_prefix[r][c] + grid[r][c]
                col_prefix[c][r + 1] = col_prefix[c][r] + grid[r][c]

        def row_sum(r: int, left: int, right: int) -> int:
            return row_prefix[r][right + 1] - row_prefix[r][left]

        def col_sum(c: int, top: int, bottom: int) -> int:
            return col_prefix[c][bottom + 1] - col_prefix[c][top]

        def is_magic(top: int, left: int, size: int) -> bool:
            bottom = top + size - 1
            right = left + size - 1

            target = row_sum(top, left, right)

            # Check all rows.
            for r in range(top + 1, bottom + 1):
                if row_sum(r, left, right) != target:
                    return False

            # Check all columns.
            for c in range(left, right + 1):
                if col_sum(c, top, bottom) != target:
                    return False

            main_diag = 0
            anti_diag = 0

            for offset in range(size):
                main_diag += grid[top + offset][left + offset]
                anti_diag += grid[top + offset][right - offset]

            return main_diag == target and anti_diag == target

        # Try larger sizes first so we can return immediately.
        for size in range(min(m, n), 0, -1):
            for top in range(m - size + 1):
                for left in range(n - size + 1):
                    if is_magic(top, left, size):
                        return size

        return 1