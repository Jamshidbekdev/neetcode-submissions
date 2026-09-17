class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = {}
        for ch in s1:
            mp1[ch] = 1 + mp1.get(ch, 0)
        mp2 = {}
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        while r < len(s2):
            mp2[s2[r]] = 1 + mp2.get(s2[r], 0)
            # print('mp1 ', mp1)
            # print('mp2 ', mp2)
            print('(r - l + 1) = ', r - l + 1)
            print('len(s1) ', len(s1))

            if r - l + 1 > len(s1):
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
            if r - l + 1 == len(s1) and mp2 == mp1:
                return True
            r += 1
        return False
        