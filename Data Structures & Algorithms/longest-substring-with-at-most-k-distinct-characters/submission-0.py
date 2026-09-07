class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        window = {}
        result = 0
        while r < len(s):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            r += 1
            while len(window) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            result = max(result, r - l)
        return result