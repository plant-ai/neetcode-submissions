class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if (yesterday := prices[i-1]) < (today := prices[i]):
                profit += today - yesterday
        return profit