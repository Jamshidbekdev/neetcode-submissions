class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 1;
        temp = strs[0];
        for c in range(len(temp)):
            piece = temp[c]
            for word in strs[1:]:
                if len(word) == c or piece != word[c]:
                    return temp[:c]
        return temp