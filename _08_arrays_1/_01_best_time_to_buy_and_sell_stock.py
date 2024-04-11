#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = 0
        g = 0
        for i in range(1, len(prices)):
            f = max(0, f) + prices[i] - prices[i-1]
            g = max(f, g)
        return g
