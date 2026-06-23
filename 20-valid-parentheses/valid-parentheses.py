class Solution:
    def isValid(self, s: str) -> bool:
        '''
        valid if all opening are matched with closing 
        maintain a stack;
        - if open push to stack 
        - if close 
            check if stack not empty and top is a matching opening 
            else return false
        '''
        stack = [] 
        mapping = {')': '(', '}': '{', ']':'['}
        for char in s: 
            if char in ['(', '{', '[']: 
                stack.append(char) 
            else: 
                if stack and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False 
        return len(stack) == 0
        