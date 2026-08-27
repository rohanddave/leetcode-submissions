class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        counts = [[] for _ in range(n + 1)]
        counter = collections.Counter(s)
        for char, freq in counter.items():
            counts[freq].extend(char * freq)
        res = []
        for i in range(n, -1, -1):
            if len(counts[i]) > 0:
                res.extend(counts[i])
        
        return ''.join(res)

        


        