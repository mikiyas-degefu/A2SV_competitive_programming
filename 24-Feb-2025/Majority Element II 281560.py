# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_appear = defaultdict(int)
        result = []
        n = len(nums) // 3
        for num in nums:
            nums_appear[num]+=1
        
        for key, val in nums_appear.items():
            if val > n:
                result.append(key)
        
        return result
        
        

        