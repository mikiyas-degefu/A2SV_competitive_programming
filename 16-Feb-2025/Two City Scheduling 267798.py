# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

from collections import defaultdict
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        priority_key = defaultdict(int)

        for i,cost in enumerate(costs):
            priority_key[i] = cost[0] - cost[1]

        priority = sorted(priority_key.items(), key = lambda x : x[1])

        lg = len(costs) // 2
        result = 0
        for i in range(lg):
            city_a = priority[i][0]
            city_b = priority[ lg + i][0]

            result+= costs[city_a][0]
            result+= costs[city_b][1]
            
        return result


        