class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mi , ma = 1 , max(piles)
        res = ma

        while mi <= ma:
            mid = (mi + ma) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                res = mid
                ma = mid - 1
            else:
                mi = mid + 1
            
        return res