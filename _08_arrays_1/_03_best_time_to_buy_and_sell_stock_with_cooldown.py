#309. Best Time to Buy and Sell Stock with Cooldown
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        g = 0
        f = 0
        queue = deque([0] * 3)
        for i in range(1, len(prices)):
            f = prices[i] - prices[i - 1] + max(f, queue.popleft())
            g = max(g, f)
            queue.append(g)
        return g
