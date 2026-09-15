class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        n = len(words)
        l = 0 
        curr_char_count = 0
        res = []
        curr = []
        
        for r in range(n):
            word_count = r - l + 1
            min_number_of_spaces_required = word_count - 1
            new_char_count = curr_char_count + len(words[r])
            # include this word in the current sequenece
            if new_char_count + min_number_of_spaces_required <= maxWidth:
                curr.append(words[r])
                curr_char_count = new_char_count
            else: 
                # start a new sequence 
                total_spaces_required = maxWidth - curr_char_count # spaces req to make = maxWidth
                gaps = len(curr) - 1
                if gaps == 0: 
                    curr_str = curr[0] + ' ' * total_spaces_required
                else: 
                    spaces_between_words = total_spaces_required // gaps # divide spaces required between gaps
                    extra_spaces = total_spaces_required % gaps
                    # construct the word str
                    curr_str = ''
                    for i, word in enumerate(curr): 
                        curr_str += word 
                        if i < gaps:
                            spaces = spaces_between_words
                            if i < extra_spaces: 
                                spaces += 1
                            curr_str += ' ' * spaces

                res.append(curr_str)

                # start a new sequenece with the current word
                curr = [words[r]] 
                curr_char_count = len(words[r])
                l = r
        last_line = ' '.join(curr)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        return res

            
            

        