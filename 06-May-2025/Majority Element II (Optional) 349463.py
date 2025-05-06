# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = Counter(nums)
        result = []

        for key,val in count.items():
            if val > len(nums)/3:
                result.append(key)

        return result