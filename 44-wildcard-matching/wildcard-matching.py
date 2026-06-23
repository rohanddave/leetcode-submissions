class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        dfs fn returns true or false if the pattern is matched 

        base case: if we reach the end of s and end of p then return true 
        base case: if p[j] is a character and does not match s[i] return false 
        - if p[j] is character and matches s[i] increment i, j 
        - if p[j] is ? increment i, j regardless 
        - if p[j] is * 
            - match empty increment j 
            - match one char increment i
        '''
        new_p = [] 
        i = 0
        while i < len(p): 
            if p[i].isalpha() or p[i] == '?':
                new_p.append(p[i])
                i += 1
            else: 
                new_p.append(p[i])
                while i < len(p) and p[i] == "*":
                    i += 1
        p = ''.join(new_p)

        memo = {}
        def dfs(i, j): 
            if i == len(s) and j == len(p):
                return True 
            if j == len(p):
                return i == len(s)
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s):
                memo[(i, j)] = all(char == "*" for char in p[j:]) 
            elif p[j].isalpha() and p[j] != s[i]: 
                memo[(i, j)] = False 
            elif (p[j].isalpha() and p[j] == s[i]) or p[j] == '?':
                memo[(i, j)] = dfs(i + 1, j + 1)
            else: 
                match_empty = dfs(i, j + 1)
                match_char = dfs(i + 1, j)
                memo[(i, j)] = match_empty or match_char
            return memo[(i, j)]
        return dfs(0, 0)
            
        