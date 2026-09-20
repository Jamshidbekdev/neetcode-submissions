class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = {}
        l, r = 0, 0
        res = 0
        while r < len(fruits):
            mp[fruits[r]] = mp.get(fruits[r], 0) + 1
            while len(mp) > 2:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] == 0:
                    del mp[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
        