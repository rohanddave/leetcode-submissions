class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)

        for string in strs: 
            counts = [0] * 26
            for char in string: 
                counts[ord(char) - ord('a')] += 1
            key = ''
            for i, count in enumerate(counts): 
                key += str(count) + chr(ord('a') + i)

            mapping[key].append(string)
        
        return [mapping[key] for key in mapping.keys()]
        