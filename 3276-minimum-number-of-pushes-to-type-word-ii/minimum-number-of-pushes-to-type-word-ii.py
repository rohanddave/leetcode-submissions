class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = collections.Counter(word)
        max_heap_characters = [(-freq,char) for char, freq in counter.items()]
        heapq.heapify(max_heap_characters)

        min_heap_numbers = [(0, num) for num in range(2, 10)]
        heapq.heapify(min_heap_numbers)

        res = 0

        while max_heap_characters: 
            neg_freq, char = heapq.heappop(max_heap_characters)
            freq = -1 * neg_freq 

            count, num = heapq.heappop(min_heap_numbers)
            new_count = count + 1

            heapq.heappush(min_heap_numbers, (new_count, num))

            res += freq * new_count
        
        return res



        