# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_seen = defaultdict(int)
        mod_seen[0] = 1
        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k


            if rem in mod_seen:
                result+=mod_seen[rem]
            mod_seen[rem]+=1

        return result