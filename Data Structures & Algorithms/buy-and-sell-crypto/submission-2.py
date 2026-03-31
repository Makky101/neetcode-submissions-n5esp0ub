class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            r = len(prices) - 1
            while r != i:
                total = prices[r] - prices[i]
                profit = max(profit, total)
                r -= 1
        if profit < 0:
            profit = 0
        return profit