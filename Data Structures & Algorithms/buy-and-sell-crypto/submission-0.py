class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            difference = max(prices[i::]) - prices[i]
            if profit < difference:
                profit = difference
        return profit
