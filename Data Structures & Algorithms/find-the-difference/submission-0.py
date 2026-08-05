class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        for i in s:
            mp[i] = mp.get(i, 0) + 1
        for i in range(len(t)):
            char = t[i]
            if char in mp and mp[char] > 0:
                mp[char] -= 1
            else:
                return char

        for i, v in mp.items():
            if v > 0:
                return i
        return ''