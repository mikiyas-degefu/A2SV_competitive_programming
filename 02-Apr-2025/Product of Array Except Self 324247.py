# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        total_pdt = 1
        result = []

        for num in nums:
            if num == 0:
                count_zero+=1
            else:
                total_pdt *= num
        
        if count_zero > 1:
            return [0] * len(nums)
        elif count_zero == 1:

            for num in nums:
                if num == 0:
                    result.append(total_pdt)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(total_pdt // num)
        
        return result
        
        