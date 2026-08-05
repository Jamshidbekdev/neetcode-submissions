class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1 = pt2 = 0
        result = ''
        while pt1 < len(word1) and pt2 < len(word2):
            result += word1[pt1]
            result += word2[pt2]
            pt1 += 1
            pt2 += 1
        result += word1[pt1:]
        result += word2[pt2:]
        return result