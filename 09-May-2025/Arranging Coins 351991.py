# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            cur = (mid * (mid + 1)) // 2 

            if cur == n:
                return mid
            elif cur < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right 
        