# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_seen = {0 : -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            mod = prefix_sum % k
            if mod in mod_seen:
                if i - mod_seen[mod] > 1:
                    return True
            else:
                mod_seen[mod] = i


        return False

        

