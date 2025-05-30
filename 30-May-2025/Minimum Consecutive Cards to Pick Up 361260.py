# Problem: Minimum Consecutive Cards to Pick Up - https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        positions = defaultdict(int)
        res = float('inf')
        for i,card in enumerate(cards):
            if card in positions:
                res = min(res, i - positions[card] + 1)
            positions[card] = i

        
        if res == float('inf'):
            return -1
        return res
        