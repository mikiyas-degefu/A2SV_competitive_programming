# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = defaultdict(int)
        total = 0
        count = 0

        sub_num[0] += 1

        for num in nums:
            total += num

            
            if total - k in sub_num:
                count += sub_num[total - k]
            
            sub_num[total] += 1
        
        print(sub_num)
        return count
        

