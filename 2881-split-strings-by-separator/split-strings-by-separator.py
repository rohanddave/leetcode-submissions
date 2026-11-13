class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words: 
            for word in word.split(separator):
                if len(word): 
                    res.append(word)
        return res