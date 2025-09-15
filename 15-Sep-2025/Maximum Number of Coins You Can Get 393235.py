# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_num = 0
        while len(piles) > 0:
            piles.pop()
            max_num+=piles[len(piles) - 1]
            piles.pop()
            piles.pop(0)
        
        return max_num
