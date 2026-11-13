class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set() 

        def dfs(i, j): 
            if i + j == target:
                return True 
            if (i, j) in visited:
                return False
            
            visited.add((i, j))
            
            res = False 

            # fill i
            if i < x and dfs(x, j):
                return True 
            # fill j
            if j < y and dfs(i, y):
                return True
            
            if i != 0 and dfs(0, j):
                return True

            if j != 0 and dfs(i, 0):
                return True

            # pour from i -> j
            amt = min(i, y - j)
            if amt > 0 and dfs(i - amt, j + amt):
                return True
            
            # pur from j -> i
            amt = min(j, x - i)
            if amt > 0 and dfs(i + amt, j - amt):
                return True
            
            return False
        
        return dfs(0, 0)