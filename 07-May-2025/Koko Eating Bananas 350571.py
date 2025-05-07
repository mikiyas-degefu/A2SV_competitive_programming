# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            #iterate through the array and calculate the hours
            for pill in piles:
                hours += math.ceil(pill / mid)

            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
                