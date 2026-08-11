class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        '''
        problem: 
        - binary string
        - 0 = inactive; 1 = active 
        - at most one trade to maximize number of sections, where trade =
            - convert contiguous block of 1's surrounded by 0's to 0's 
            - convert a contiguous block of 0's surrounded by 1's to 1's 
        
        goal: return max number of active sections

        observations: 
        - assume string s is surrounded by 1's i.e. '1' + s + '1'
        - number of active sections = number of 1's in the string 
        - to get maximum number of active sections we need to convert a contiguous 1's that would form the largest contiguous 0's
        
        s = "1000100"
        prefix = [0,1,2,3,3,4,5]
        suffix = [5,5,4,3,2,2,1]

        (1, 1), (0, 3), (1, 1), (0, 2)


        '''
        n = len(s)
        sections = []

        i = 0 
        while i < n:  
            j = i + 1 
            while j < n and s[j] == s[i]: 
                j += 1
            sections.append((s[i], j - i))
            i = j
        
        res = 0
        for i in range(n):
            if s[i] == '1': 
                res += 1
            
        largest_contr = 0
        for idx, (element, count) in enumerate(sections): 
            prev_element = sections[idx - 1][0] if idx > 0 else '1'
            next_element = sections[idx + 1][0] if (idx + 1) < len(sections) else '1'

            if element == '1' and prev_element == '0' and next_element == '0':
                prev_count = sections[idx - 1][1]
                next_count = sections[idx + 1][1]
                largest_contr = max(largest_contr, prev_count + next_count)
        
        return res + largest_contr