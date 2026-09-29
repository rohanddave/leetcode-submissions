class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        '''
        observations: 
        - there is no explicit matrix to work on 
        - left to right UF will not work since we would need a un-union operation
        - left to right binary search will not work unless all cells before the current position are considered
        - all we care about is connectivity not the path itself, makes UF a strong candidate 

        approach: 
        - iterate from the end of cells 
        - prepare a UF data structure and union all (r,c) with nei 0 cells 
        '''
        def can(x): 
            q = collections.deque()
            visited = set()
            obstacles = set()
            
            for i in range(x): 
                obstacles.add((cells[i][0], cells[i][1]))
        
            for i in range(col): 
                point = (1, i + 1) 
                if point not in obstacles:
                    q.append((1, i + 1))
                    visited.add((1, i + 1))
            
            while q:
                r, c = q.popleft() 

                # reached the last row
                if r == row:
                    return True 

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc 
                    if 1 <= nr <= row and 1 <= nc <= col and (nr, nc) not in obstacles and (nr, nc) not in visited: 
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return False 
        
        l, r = 0, len(cells)
        while l < r:
            m = (l + r) // 2
            if not can(m): 
                r = m 
            else:
                l = m + 1
        return l - 1
        