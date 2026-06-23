class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        when building valid paranthesis if c < o then it is not possible to create a valid formation
        that means c >= o
        '''
        res = []
        def dfs(o, c, current):
            if o == 0 and c == 0:
                res.append(''.join(current))
                return 
            if c < o:
                return
            
            if o > 0:
                current.append('(')
                dfs(o - 1, c, current)
                current.pop()
            
            if c > 0:
                current.append(')')
                dfs(o, c - 1, current)
                current.pop()
        dfs(n, n, [])
        return res


        