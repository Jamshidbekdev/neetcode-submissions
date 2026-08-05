class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result = [0] * 26

        for index in range(len(s)):
            result[ord(s[index]) - ord('a')] += 1
            result[ord(t[index]) - ord('a')] -= 1
        
        for item in result:
            if item != 0:
                return False
        return True