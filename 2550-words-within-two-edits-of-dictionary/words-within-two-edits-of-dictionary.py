class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            for dict_word in dictionary: 
                diff = 0
                for i in range(len(query)): 
                    if query[i] != dict_word[i]:
                        diff += 1
                    
                    if diff > 2: 
                        break
                
                if diff <= 2:
                    res.append(query) 
                    break
        return res


