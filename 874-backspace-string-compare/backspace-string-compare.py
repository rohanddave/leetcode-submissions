class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = [] 
        for char in s: 
            if char == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(char)

        t_stack = [] 
        for char in t: 
            if char == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(char)
        
        print(s_stack, t_stack)
        return s_stack == t_stack

        