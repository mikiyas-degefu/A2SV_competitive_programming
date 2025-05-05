# Problem: Heaters  - https://leetcode.com/problems/heaters/

from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)

        def minDist(house) -> int:
            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] == house:
                    return 0
                elif heaters[mid] > house:
                    r = mid - 1
                else:
                    l = mid + 1
            
            left_dist = abs(house - heaters[r]) if r >= 0 else float('inf')
            right_dist = abs(heaters[l] - house) if l < n else float('inf')

            return min(left_dist, right_dist)
        
        nearest = [minDist(house) for house in houses]
        print(nearest)
        return max(nearest)
