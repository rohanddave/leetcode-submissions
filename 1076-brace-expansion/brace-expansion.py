class Solution:
    def expand(self, s: str) -> list[str]:
        adj = []
        i = 0

        while i < len(s): 
            if s[i] == '{':
                i += 1
                options = []
                while s[i] != '}':
                    if s[i] != ',':
                        options.append(s[i])
                    i += 1
                adj.append(options)
            else:
                adj.append([s[i]])
            i += 1

        res = []
        def dfs(i, curr): 
            if i == len(adj): 
                res.append(''.join(curr[:]))
                return
            
            for char in sorted(adj[i]):
                curr.append(char)
                dfs(i + 1, curr)
                curr.pop()

        dfs(0, [])               

        return res


        