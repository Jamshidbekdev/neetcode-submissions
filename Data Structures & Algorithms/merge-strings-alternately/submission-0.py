class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1, pt2 = 0, 0
        s = ""
        while pt1 < len(word1) and pt2 < len(word2):
            s += word1[pt1]
            s += word2[pt2]
            pt1 += 1
            pt2 += 1
        if pt1 == len(word1):
            s += word2[pt2:]
        if pt2 == len(word2):
            s += word1[pt1:]

        return s