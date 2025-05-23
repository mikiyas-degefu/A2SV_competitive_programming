# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_string = [str(num)  for num in nums]
        sorted_nums = sorted(num_string, key = lambda x : x * 10, reverse = True)

        if sorted_nums[0] == '0':
            return '0'
        
        return "".join(sorted_nums)
        