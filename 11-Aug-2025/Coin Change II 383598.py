# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)

    
        def dp(remaining, i):
            if remaining == 0:
                return 1
            if remaining < 0 or i >= len(coins):
                return 0
            if (remaining, i) in memo:
                return memo[(remaining, i)]

            take = dp(remaining - coins[i], i)      
            skip = dp(remaining, i + 1)             

            memo[(remaining, i)] = take + skip
            return memo[(remaining, i)]

        return dp(amount, 0)
        