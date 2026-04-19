class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for day_price in prices:
            if day_price < buy:
                buy = day_price
            if day_price - buy > profit:
                profit = day_price - buy
        return profit