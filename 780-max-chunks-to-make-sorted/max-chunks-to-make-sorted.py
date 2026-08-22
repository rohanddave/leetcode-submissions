class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        observations: 
        - permutation of [0, n - 1]
        - 

        nums=  [1,0,2,3,4]
        
        '''
        max_seen = float('-inf')
        chunks = 0
        for i, num in enumerate(arr): 
            max_seen = max(max_seen, num)
            if max_seen == i:
                chunks += 1

        return chunks