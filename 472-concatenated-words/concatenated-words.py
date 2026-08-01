class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        goal: return all concatenated words
        '''
        word_set = set(words)

        # i = index of word; j = start position of words[i]
        memo = {}
        def dfs(word):
            if len(word) == 0:
                return 1
            if word in memo:
                return memo[word]
            
            count = 0
            for k in range(1, len(word) + 1):
                prefix = word[:k]
                if prefix in word_set:
                    count += dfs(word[k:])
            memo[word] = count   
            return memo[word]
        
        answer = []
        for i, word in enumerate(words):
            if dfs(word) > 1:
                answer.append(word)
        return answer
        