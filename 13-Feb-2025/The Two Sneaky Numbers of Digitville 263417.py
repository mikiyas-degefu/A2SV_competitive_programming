# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        count_occr = {}
        result = set()

        for i in nums:
            if i in count_occr:
                result.add(i)
            else:
                count_occr[i] = 1
        
        return list(result)

        