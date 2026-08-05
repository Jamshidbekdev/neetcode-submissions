class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        count = 0
        for index, value in mp.items():
            if value % 2 != 0:
                count += 1
        if count > 1:
            return False
        return True