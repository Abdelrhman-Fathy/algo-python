#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        g = 0
        for i in range(1, len(prices)):
            g = g + max(0, prices[i] - prices[i - 1])
        return g

