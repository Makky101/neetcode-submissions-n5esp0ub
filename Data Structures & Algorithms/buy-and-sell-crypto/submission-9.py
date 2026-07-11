class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,l = 1,0
        res_max = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                res_max = max(res_max, p)
            else:
                l = r
            r+=1
        return res_max

        
