# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        occurance = Counter(nums)
        count = 0
        item_left = 0
        for key, val in occurance.items():
            if val % 2 == 0:
                count+=(val//2)
            else:
                item_left+=(val%2)
                value = ((val - val%2) // 2)
                count+= value if val > 1 else 0
        
        return [count,item_left ]
                



        