class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        goal: return string of unique letters sorted in lexicographically increasing order according the alien language rules 

        t -> f
        w -> e 
        r -> t 
        e -> r

        w -> e -> r -> t -> f 
        '''
        
        chars = set() 

        for word in words: 
            for ch in word: 
                chars.add(ch)
        
        adj = {}
        in_degree = {}

        for char in chars: 
            adj[char] = set() 
            in_degree[char] = 0
        
        for i in range(len(words) - 1): 
            curr, nex = words[i], words[i + 1]
            j = 0
            while j < min(len(curr), len(nex)) and curr[j] == nex[j]:
                j += 1
            
            if j == min(len(curr), len(nex)):
                if len(curr) > len(nex):
                    return ''
                continue
            
            u, v = curr[j], nex[j]
            if v not in adj[u]:
                adj[u].add(v)
                in_degree[v] += 1

        q = collections.deque()

        for char, in_deg in in_degree.items():
            if in_deg == 0:
                q.append(char)
        
        res = []
        while q: 
            char = q.popleft() 
            res.append(char)

            for nei in adj[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return ''.join(res) if len(res) == len(chars) else ''


        