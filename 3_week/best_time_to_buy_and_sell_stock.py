class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = float('inf'), 0
        for price in prices:
            buy, profit = min(buy, price), max(profit, price - buy)
        return profit

#         Solution 1
#         if not prices: return 0
#         buy_price, sell_price, profit = prices[0], 0, 0
#         for idx, val in enumerate(prices[1:]):
#             if val - buy_price > profit:
#                 profit = val - buy_price
#                 sell_price = val
#             elif val < buy_price:
#                 buy_price = val

#         return profit

