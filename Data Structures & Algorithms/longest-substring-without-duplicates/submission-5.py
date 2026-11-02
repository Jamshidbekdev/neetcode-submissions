class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        seen = {}
        l = 0
        longest_length = 0
        for r, v in enumerate(s):
            if v in seen and seen[v] >= l:
                l = seen[v] + 1
            longest_length = max(longest_length, r - l + 1)
            seen[v] = r

        return longest_length