class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 1000000000
        maxx = -1 
        for price in prices:
            minn = min(minn, price)
            maxx = max(maxx, price - minn)
        return maxx