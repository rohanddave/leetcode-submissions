class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(string):
            res = ''
            count = 1
            curr_char = string[0]

            for i in range(1, len(string)): 
                if string[i] == curr_char: 
                    count += 1
                else:
                    res += str(count) + curr_char
                    count = 1
                    curr_char = string[i]

            return res +str(count) + curr_char
        
        def count_and_say(n):
            if n == 1:
                return "1"
            return rle(count_and_say(n - 1))

        return count_and_say(n)

        