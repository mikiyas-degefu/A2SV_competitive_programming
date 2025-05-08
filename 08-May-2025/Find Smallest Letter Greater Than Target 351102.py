# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    
        n = len(letters)
        left = 0
        right = n - 1
        res = letters[0]

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while left <= right:
            mid = (left + right) // 2

            if target >= letters[mid]:
                left = mid + 1

            if target < letters[mid]:
                right = mid - 1

        return letters[left] 
            
        