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
        heap = [(abs(self.mapping[word1][0] - self.mapping[word2][0]), 0, 0)] 
        res = float('inf')
        while heap: 
            val, i, j = heapq.heappop(heap)
            res = min(res, val) 

            if j + 1 < len(self.mapping[word2]): 
                heapq.heappush(heap, (abs(self.mapping[word1][i] - self.mapping[word2][j + 1]), i, j + 1))
            
            if i + 1 < len(self.mapping[word1]):
                heapq.heappush(heap, (abs(self.mapping[word1][i + 1] - self.mapping[word2][j]), i + 1, j))
            
        return res






# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)