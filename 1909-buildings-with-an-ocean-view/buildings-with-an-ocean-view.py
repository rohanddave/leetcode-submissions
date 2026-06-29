class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        goal: return list of 0 indexed buildings that have an ocean view in increasing order 

        observation: 
        - ith building has ocean view if heights[i + 1: ] < heights[i]
        '''
        res = []
        max_seen = float('-inf')
        for i in range(len(heights) - 1, -1, -1):
            if max_seen < heights[i]:
                res.append(i)
            max_seen = max(max_seen, heights[i])
        
        return res[::-1]

