# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num
        
        diff_bit = 1

        while not(diff_bit & xor):
            diff_bit = 1 << diff_bit
        
        group_a, group_b = 0,0

        for num in nums:
            if num & diff_bit:
                group_a ^= num
            else:
                group_b ^= num

        return [group_a, group_b]