class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            count = 1
            summ = 0
            for w in weights:
                if summ + w > mid:
                    count += 1
                    summ = 0
                summ += w
            if count <= days:
                r = mid
            else:
                l = mid + 1
        return l