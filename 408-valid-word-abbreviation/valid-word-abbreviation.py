class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        curr_abbr = ''

        while j < len(abbr):
            if not abbr[j].isdigit():
                if i >= len(word) or abbr[j] != word[i]:
                    print('early returning false: ', i, j)
                    return False
                i += 1
                j += 1
            else:
                number = ''
                while j < len(abbr) and abbr[j].isdigit():
                    number += abbr[j]
                    j += 1
                if number[0] == '0':
                    return False
                i += int(number)
            # i += 1
            # j += 1
        return i == len(word)
        