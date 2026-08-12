class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque([(0, 0, 0)]) 
        visited = {(0, 0)}

        while q: 
            dist, curr_x, curr_y = q.popleft() 

            if curr_x == x and curr_y == y:
                return dist 
            
            neighbors = [(curr_x - 2, curr_y + 1), (curr_x + 2, curr_y + 1), (curr_x - 1, curr_y + 2), (curr_x + 1, curr_y + 2), (curr_x - 2, curr_y - 1), (curr_x + 2, curr_y - 1), (curr_x - 1, curr_y - 2), (curr_x + 1, curr_y - 2)]

            for nei_x, nei_y in neighbors: 
                if (nei_x, nei_y) not in visited:
                    q.append((dist + 1, nei_x, nei_y))
                    visited.add((nei_x, nei_y))
        
        


        