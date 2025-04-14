# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num//3
        result = [x - 1, x, x + 1]

        return result if sum(result) == num else []

  