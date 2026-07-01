class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        '''
        goal: return full substituted text string which does not contain any placeholders 

        example: 
        Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"
        Output: "abc_def"

        Input: replacements = [["A","bce"],["B","ace"],["C","abc%B%"]], text = "%A%_%B%_%C%"
        Output: "bce_ace_abcace"

        observations:
        - each replacement itself might contain variables 
        - a variable can be substituted once it's substituion string does not contain any variables 
        - if ["C","abc%B%"] that means C depends on B i.e. we need to resolve B to get the value of C
        '''

        i = 0
        res = []

        replacements_map = {var: replacement for var, replacement in replacements}
        memo = {}
        def dfs(var): 
            if var in memo:
                return memo[var]
            
            i = 0
            answer = []
            replacement_str = replacements_map[var]
            while i < len(replacement_str):
                if replacement_str[i] == '%':
                    i += 1
                    dep_var = ''
                    while replacement_str[i] != '%':
                        dep_var += replacement_str[i]
                        i += 1
                    answer.extend(dfs(dep_var))
                    i += 1               
                else: 
                    answer.append(replacement_str[i])
                    i += 1
            return ''.join(answer)

        while i < len(text): 
            if text[i] == '%':
                i += 1
                var = ''
                while text[i] != '%':
                    var += text[i]
                    i += 1
                res.extend(dfs(var))
                i += 1               
            else: 
                res.append(text[i])
                i += 1
        return ''.join(res)

