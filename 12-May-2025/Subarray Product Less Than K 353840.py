# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        product = 1
        left = 0

        if k <= 1:
            return 0

        for right, num in enumerate(nums):
            product *= num

            while product >= k and left < len(nums):
                product //= nums[left]
                left += 1
            
            count += right - left + 1

        return count


        
        