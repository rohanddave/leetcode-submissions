class WordDistance:

    def __init__(self, wordsDict: List[str]):
        '''
        observations: 
        - what happens when there are duplicates in the list? 
        '''
        self.mapping = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.mapping[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        for i in self.mapping[word1]:
            for j in self.mapping[word2]: 
                res = min(res, abs(i - j))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)