class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        '''
        0 => empty 
        1 => wall 

        - ball keeps rolling in same direction till it hits a wall
        - once it hits a wall choose direction (cannot be the same as previous one)
        - ball will fall into the hole
        - shortest path from ball to hole but the lexicographically smallest instruction string
        - distance = number of empty spaces traveled by the ball 

        example: ul -> 6 and lul -> 6 but return lul because l < u

        approach: 
        - use dijkstra for shortest path where the min heap stores (cost, instruction, r, c)
        - cost is the distance of rolling from start to either a wall or the hole
        - when exploring neighbors try all directions except the previously popped from the heap
        '''
        m, n = len(maze), len(maze[0])
        start = (0, "", ball[0], ball[1])
        best = {(ball[0], ball[1]): (0, "")} 
        heap = [start]
        directions = [(1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')]

        while heap: 
            dist, path, r, c = heapq.heappop(heap)

            if r == hole[0] and c == hole[1]:
                return path 
            
            if (dist, path) > best[(r ,c)]:
                continue

            for dr, dc, p in directions:
                nr, nc = r, c 
                roll_dist = 0
                while True:
                    tr, tc = nr + dr, nc + dc

                    if not (0 <= tr < m and 0 <= tc < n):
                        break
                    if maze[tr][tc] == 1:
                        break

                    nr = tr
                    nc = tc
                    roll_dist += 1

                    if (nr, nc) == tuple(hole):
                        break

                nei_dist = dist + roll_dist
                nei_path = path + p
                if (nei_dist, nei_path) < best.get((nr, nc), (float("inf"), "~")):
                    heapq.heappush(heap, (nei_dist, nei_path, nr, nc))
                    best[(nr, nc)] = (nei_dist, nei_path)
        
        return "impossible"


