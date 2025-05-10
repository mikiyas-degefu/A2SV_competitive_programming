# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def count_days(mid):
            count_days = 1
            curr_sum = 0

            for weight in weights:

                if curr_sum + weight > mid:
                    count_days += 1
                    curr_sum = 0
                
                curr_sum += weight

            return count_days

        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            cur_days = count_days(mid)

            if cur_days <= days:
                high = mid
            else:
                low = mid + 1
            
        return low


