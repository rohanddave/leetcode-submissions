class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        problem: 
        - citations[i] = number of citations researcher received for ith paper 

        goal: return h-index 

        TTFFF
        '''
        def can(x): 
            count = 0
            for citation in citations: 
                if citation >= x:
                    count += 1
            return count >= x

        
        l, r = 0, len(citations) + 1
        while l < r: 
            m = (l + r) // 2
            if not can(m):
                r = m
            else:
                l = m + 1
        return l - 1


        