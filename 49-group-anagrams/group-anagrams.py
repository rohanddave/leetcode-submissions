class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs: 
            count = [0] * 26
            for char in s: 
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key not in m: 
                m[key] = []
            m[key].append(s)

        return list(m.values())

        