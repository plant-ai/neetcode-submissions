class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # naive we can just find min max 
        # starting to slide increasing sizes of sliding windows across to get the profit at each index if you were to sell 
        # kinda makes this triangular matrix
        # not sure how to do without blowing up
        profit = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit