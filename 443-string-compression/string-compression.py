class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        # if only one character
        if n == 1:
            return 1
        
        count, curr_idx = 1, 0
        for i in range(1, n):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                # write the previous character
                chars[curr_idx] = chars[i - 1]
                curr_idx += 1
                # write previous character count as a string of characters
                if count > 1:
                    for char in str(count): 
                        chars[curr_idx] = char
                        curr_idx += 1
                # set count of current char = 1
                count = 1
        
        # if count > 1:
        chars[curr_idx] = chars[-1]
        curr_idx += 1
        if count > 1:
            for char in str(count): 
                chars[curr_idx] = char
                curr_idx += 1

        return curr_idx


        