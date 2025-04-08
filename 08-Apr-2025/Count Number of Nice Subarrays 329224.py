# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        sub_arrays = 0
        prefix_sum = defaultdict(int)
        prefix_sum[cur_sum] = 1

        for i in range(len(nums)):
            cur_sum += nums[i] % 2

            if cur_sum - k in prefix_sum:
                sub_arrays += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] += 1
        
        return sub_arrays


        
        