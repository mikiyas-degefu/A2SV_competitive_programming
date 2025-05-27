# Problem: Boats To Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        min_carry = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  
            right -= 1  
            min_carry += 1 

        return min_carry
        