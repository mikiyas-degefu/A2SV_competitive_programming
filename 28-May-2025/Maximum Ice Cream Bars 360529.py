# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        costs.sort()

        total_cost = 0
        for cost in costs:
            total_cost += cost
            if total_cost > coins:
                break
            res += 1
        
        return res

        