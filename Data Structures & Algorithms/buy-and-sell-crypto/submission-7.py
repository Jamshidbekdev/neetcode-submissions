class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #    [10,1,5,6,7,1]
    #        l
    #               r
        l, r = 0, 0
        maxx = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            maxx = max(maxx, prices[r] - prices[l])
            r += 1
        return maxx