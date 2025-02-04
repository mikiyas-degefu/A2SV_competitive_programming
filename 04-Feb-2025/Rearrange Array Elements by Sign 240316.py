# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)
        pos_index = 0
        neg_index = 1

        for num in nums:
            if num > -1:
                result[pos_index] = num
                pos_index+=2
            else:
                result[neg_index] = num
                neg_index+=2

        return result


        