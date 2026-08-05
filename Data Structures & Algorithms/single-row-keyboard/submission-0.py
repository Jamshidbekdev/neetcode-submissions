class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mp = {}
        result = 0
        for index, char in enumerate(keyboard):
            mp[char] = index
        temp = 0
        for letter in word:
            result += abs(mp[letter] - temp)
            temp = mp[letter]
        return result;