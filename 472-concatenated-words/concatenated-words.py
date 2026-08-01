class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        goal: return all concatenated words


        '''
        word_set = set(words)

        # i = index of word; j = start position of words[i]
        memo = {}
        def dfs(i, j):
            if j == len(words[i]):
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            count = 0
            for k in range(j + 1, len(words[i]) + 1):
                substring = words[i][j: k]
                if substring in word_set:
                    count += dfs(i, k)
            memo[(i, j)] = count   
            return memo[(i, j)]
        
        answer = []
        for i, word in enumerate(words):
            res = dfs(i, 0)
            if res > 1:
                answer.append(word)
        return answer
        