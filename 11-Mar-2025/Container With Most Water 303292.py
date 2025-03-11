# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            current = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, current)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return maxArea


