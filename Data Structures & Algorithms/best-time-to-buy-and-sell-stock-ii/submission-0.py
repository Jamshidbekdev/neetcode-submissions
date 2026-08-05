class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        summ = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                summ += prices[i] - prices[i-1]
        return summ