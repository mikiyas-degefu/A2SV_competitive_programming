# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def check(day) -> int:
            bouquet, adj = 0, 0 
            for i in bloomDay:
                if i <= day:
                    adj += 1
                else:
                    adj = 0
                
                if adj == k:
                    bouquet += 1
                    adj = 0
            return bouquet

        
        low, high = 0, max(bloomDay)
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if check(mid) >= m:
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        
        return res


        