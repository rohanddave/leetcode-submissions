class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        MAX = max(nums)

        spf = list(range(MAX + 1))

        for p in range(2, math.isqrt(MAX) + 1):
            if spf[p] == p:
                for multiple in range(p * p, MAX + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        adj = collections.defaultdict(list) # prime_number: list of indices
        def prepare_prime_teleportations(): 
            for idx, num in enumerate(nums): 
                while num > 1:
                    p = spf[num]
                    adj[p].append(idx)

                    while num % p == 0: 
                        num //= p
                
        # preprocessing
        prepare_prime_teleportations()

        # bfs 
        q = collections.deque([(0, 0)]) # (idx, jumps)
        visited = {0} # idx

        while q: 
            node, jumps = q.popleft() 

            if node == n - 1: 
                return jumps
            
            neis = {node + 1, node - 1}
            value = nums[node]
            if value >= 2 and spf[value] == value:
                neis.update(adj.pop(value, []))

            for nei in neis: 
                if 0 <= nei < n and nei not in visited: 
                    q.append((nei, jumps + 1))
                    visited.add(nei)
            
        return -1


        