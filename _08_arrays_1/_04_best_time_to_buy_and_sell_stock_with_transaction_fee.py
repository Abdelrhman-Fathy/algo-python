#714. Best Time to Buy and Sell Stock with Transaction Fee
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f = -fee
        g = 0
        for i in range(1, len(prices)):
            f = prices[i] - prices[i - 1] + max(g - fee, f)
            g = max(g, f)
        return g


