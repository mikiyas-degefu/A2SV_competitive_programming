# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1]

        def can_place(d):
            start = float('-inf')
            count = 0
            for p in position:
                if p - start >= d:
                    start = p
                    count += 1
            
            return count >= m
            

        while left < right:
            mid = (left + right) // 2

            if can_place(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        return left

        