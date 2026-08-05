class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pt1 = pt2 = 0
        while pt2 < len(t) and pt1 < len(s):
            if t[pt2] == s[pt1]:
                pt2 += 1
            pt1 += 1
        return len(t[pt2:])