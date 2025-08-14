# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(cur_day, transactions, holding):
            if cur_day == len(prices) or transactions == 2:
                return 0
            
            if (cur_day, transactions, holding) in memo:
                return memo[(cur_day, transactions, holding)]
            
            # Option 1: Skip
            max_profit = dp(cur_day + 1, transactions, holding)
            
            # Option 2: Sell if holding
            if holding:
                max_profit = max(max_profit, dp(cur_day + 1, transactions + 1, 0) + prices[cur_day])
            # Option 3: Buy if not holding
            else:
                max_profit = max(max_profit, dp(cur_day + 1, transactions, 1) - prices[cur_day])

            memo[(cur_day, transactions, holding)] = max_profit
            return max_profit
         
        return dp(0, 0, 0)
