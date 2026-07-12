class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        '''
        wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "coding", word2 = "practice"

        word1_idx = 3, word2_idx = 0
        output = 3

        Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
        Output: 1

        word1_idx = 1, word2_idx = 3
        '''
        i1, i2 = -1, -1
        res = float('inf')

        for i, word in enumerate(wordsDict): 
            if word == word1: 
                i1 = i 
            elif word == word2:
                i2 = i 
            
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
        return res
