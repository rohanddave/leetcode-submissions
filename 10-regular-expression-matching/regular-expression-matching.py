class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        goal: return true if pattern p matches for string s 

        dfs function returns true or false if p[j:] matches s[i:]

        p[j] + '*' can match:
            1. zero occurrences of p[j]
            2. one or more occurrences of p[j], if current char matches
        '''
        memo = {}
        def dfs(i, j):  
            if j == len(p):
                return i == len(s)
            if (i, j) in memo:
                return memo[(i, j)]
            
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # if next pattern character is a *
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[(i, j)] = (
                    dfs(i, j + 2) or # use zero of p[j]
                    (first_match and dfs(i + 1, j)) 
                )
            else:
                memo[(i, j)] = first_match and (dfs(i + 1, j + 1))
            return memo[(i, j)]

        
        return dfs(0, 0)