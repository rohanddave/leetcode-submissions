class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        res = [['']* n for _ in range(numRows)]

        row, col = 0, 0
        moving_down = True

        for i, char in enumerate(s):
            res[row][col] = char 

            if row == numRows - 1:
                moving_down = False
            elif row == 0:
                moving_down = True 
            
            if moving_down: 
                row += 1
            else: 
                row -= 1
                col += 1

        res_str = ''
        
        for row in range(len(res)):
            for col in range(len(res[0])):
                res_str += res[row][col]
        return res_str

        