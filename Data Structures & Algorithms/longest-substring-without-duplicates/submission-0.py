class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        window = set()
        max_length = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length