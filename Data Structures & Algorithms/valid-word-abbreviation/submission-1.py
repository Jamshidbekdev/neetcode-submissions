class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False
            else:
                val = ''
                while j < len(abbr) and abbr[j].isdigit():
                    val += abbr[j]
                    j += 1
                i += int(val)
        return i == len(word) and j == len(abbr)
