class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res_max = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                p = prices[j] - prices[i]
                res_max = max(res_max,p,0)
        
        return res_max

        
