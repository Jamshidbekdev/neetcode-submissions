class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        mp = {}
        counter = 0
        l, r = 0, 0
        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            while mp[s[r]] > 1:
                mp[s[l]] -= 1
                l += 1
            if r - l + 1 == k:
                counter += 1
                mp[s[l]] -= 1
                l += 1
            r += 1
        return counter