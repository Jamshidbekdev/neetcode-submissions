class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = freq = best = 0
        mp = {}
        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            freq = max(freq, mp[s[r]])
            while r - l + 1 - freq > k:
                mp[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
            r += 1
        return best
