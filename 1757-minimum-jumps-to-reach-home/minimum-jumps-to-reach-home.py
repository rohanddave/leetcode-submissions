class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        '''
        goal: return minimum number of jumps needed for the bug to reach x. -1 if not possible 

        problem: 
        - exactly a jumps forward 
        - exactly b jumps backward 
        - cannot jump backwards twice in a row 
        - cannot jump to any forbidden positions 
        - may jump forward beyond its home
        - cannot jump to negative positions
        - starts at position 0
        - should end == x

        observations: 
        - if a = b then cycles exist because a -> b (forward jump) and b -> a (backward jump)- the upper bound is inf because it is allowed to jump as many forward as possible. but what if we cap it to x + max(a, b)?
        if a > b then smaller b could bring it to x 
        if b > a then also possible: example b = 2a
        - do we need to do a DP or BFS would work? since cycles are possible BFS looks safer?

        example: 
        Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
        Output: -1

        approach: 
        - bfs starting from 0
        - queue: (dist, curr_idx, is_backward?)
        - visited: (index, is_backward) because a forward move is different from a backward move
        - each cell has one maybe forward neighbor and maybe one backward neighbor (avoid negative indcies) and avoid forbidden
        - if current is a backward move then skip the backward neighbor (because two back in a row are not allowed)
        - cap the max overshoot to max(forbidden, x) + a + b
        '''
        q = collections.deque([(0, 0, False)])
        visited = {(0, False)}

        limit = max(max(forbidden), x) + a + b

        forbidden_set = set(forbidden)

        while q: 
            dist, idx, is_backward = q.popleft() 

            if idx == x:
                return dist

            neighbors = [] 
            if idx + a <= limit:
                neighbors.append((idx + a, False))
            if idx - b >= 0 and not is_backward:
                neighbors.append((idx - b, True))
            
            for nei, nei_is_backward in neighbors: 
                if nei not in forbidden_set and (nei, nei_is_backward) not in visited: 
                    q.append((dist + 1, nei, nei_is_backward))
                    visited.add((nei, nei_is_backward))
        return -1




        