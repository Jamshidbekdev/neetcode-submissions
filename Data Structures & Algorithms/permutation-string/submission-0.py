class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        j = 0
        mp1 = {}
        while j < len(s1):
            mp1[s1[j]] = 1 + mp1.get(s1[j], 0)
            j += 1
        while r < len(s2):
            if (r - l + 1 == len(s1)):
                i = l
                mp2 = {}
                while i <= r:
                    mp2[s2[i]] = 1 + mp2.get(s2[i], 0)
                    i += 1
                if mp1 == mp2:
                    return True
                l += 1
            r += 1
        return False