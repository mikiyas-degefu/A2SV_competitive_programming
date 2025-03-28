# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        unique = {}
        left = 0
        right = 0
        max_sum = 0
        win_sum = 0
        #the first sum of k
        while right < len(nums):
            if nums[right] not in unique:
                unique[nums[right]] = None
                win_sum += nums[right]
                right+=1
            else:
                unique.pop(nums[left])
                win_sum -= nums[left]
                left+=1

            if len(unique) == k:
                max_sum = max(max_sum, win_sum)
                unique.pop(nums[left])
                win_sum -= nums[left]
                left+=1
        
        return max_sum
            
