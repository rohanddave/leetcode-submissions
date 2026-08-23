class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        left, right = 0, 0
        res = float('-inf')
        window_contr = 0

        while left < len(tiles): 
            carpet_end = tiles[left][0] + carpetLen - 1

            while right < len(tiles) and tiles[right][1] <= carpet_end:
                window_contr += tiles[right][1] - tiles[right][0] + 1
                right += 1
            
            partial = 0
            if right < len(tiles) and tiles[right][0] <= carpet_end: 
                partial = carpet_end - tiles[right][0] + 1
            
            res = max(res, window_contr + partial)
            if left < right:
                window_contr -= tiles[left][1] - tiles[left][0] + 1
            else:
                right += 1
            left += 1
        
        return res
            


        