class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        '''
        observations: 
        - each move costs 1 unit of energy 
        - cycles are possible
        - same cell can be visited multiple times (augmented state)
        - whenever reach R reset energy to max capacity 
        - when can a cell be revisited? (figure out augmented state)
            - 

        S R . L
        X L X X
        '''
        m, n = len(classroom), len(classroom[0])

        def get_id(r, c): 
            return r * n + c

        start = None
        litter_id = {}
        idx = 0 

        for r in range(m):
            for c in range(n): 
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[get_id(r, c)] = idx
                    idx += 1
        
        target_mask = (1 << idx) - 1
        q = collections.deque([(0, energy, start[0], start[1], 0)]) # (moves, energy, r, c, bitmask)
        best_energy = collections.defaultdict(lambda: float('-inf')) # (r, c, bitmask)]
        best_energy[(start[0], start[1], 0)] = energy

        while q: 
            moves, curr_energy, r, c, mask = q.popleft() 

            if best_energy[(r, c, mask)] > curr_energy:
                continue

            if mask == target_mask:
                return moves
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n:
                    if classroom[nr][nc] == 'X':
                        continue
                    
                    if classroom[nr][nc] == '.' or classroom[nr][nc] == 'S':
                        if curr_energy - 1 >= 0 and best_energy[(nr, nc, mask)] < curr_energy - 1:
                            q.append((moves + 1, curr_energy - 1, nr, nc, mask))
                            best_energy[(nr, nc, mask)] = curr_energy - 1
                    elif classroom[nr][nc] == 'R':
                        if curr_energy - 1 >= 0 and best_energy[(nr, nc, mask)] < energy:
                            q.append((moves + 1, energy, nr, nc, mask))
                            best_energy[(nr, nc, mask)] = energy
                    elif classroom[nr][nc] == 'L':
                        new_mask = mask | (1 << litter_id[get_id(nr, nc)])
                        if curr_energy - 1 >= 0 and best_energy[(nr, nc, new_mask)] < curr_energy - 1:
                            q.append((moves + 1, curr_energy - 1, nr, nc, new_mask))
                            best_energy[(nr, nc, new_mask)] = curr_energy - 1

        return -1
        