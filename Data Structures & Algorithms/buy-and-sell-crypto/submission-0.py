class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = float('inf')
        maxProfit = -1
        for price in prices:
            minBuy = min(minBuy,price)
            profit = price - minBuy
            maxProfit = max(profit,maxProfit)
        return maxProfit