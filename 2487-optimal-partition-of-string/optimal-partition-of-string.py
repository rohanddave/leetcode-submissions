class Solution:
    def partitionString(self, s: str) -> int:
        window = set() 
        partitions = 0

        for right in range(len(s)): 
            if s[right] in window:
                partitions += 1
                window = set()
            window.add(s[right])
        
        return partitions + 1