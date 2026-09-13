class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minm = 100000000
        mp = {}
        l, r = 0, 0
        while r < len(blocks):
            mp[blocks[r]] = mp.get(blocks[r], 0) + 1
            if r - l + 1 == k:
                minm = min(minm, mp.get('W', 0))
                mp[blocks[l]] -= 1
                l += 1
            r += 1
        return minm