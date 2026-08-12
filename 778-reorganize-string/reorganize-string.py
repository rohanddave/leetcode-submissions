class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s) 
        heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(heap)

        pending_entry = None

        res = []

        while heap:            
            freq, char = heapq.heappop(heap)
            res.append(char)

            if pending_entry: 
                heapq.heappush(heap, pending_entry)
            
            if freq + 1 != 0:
                pending_entry = (freq + 1, char)
            else:
                pending_entry = None
        
        return ''.join(res) if pending_entry is None else ''
        