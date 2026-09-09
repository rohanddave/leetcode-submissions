class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2: 
            prev = -1 
            res = float('inf')
            for i, word in enumerate(wordsDict): 
                if word == word1:
                    if prev != -1: 
                        res = min(res, i - prev)
                    prev = i
            return res
        else: 
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
        return -1

