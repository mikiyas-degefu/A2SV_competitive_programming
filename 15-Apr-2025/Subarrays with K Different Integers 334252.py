# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)
        
    def slidingWindowAtMost(self, nums, k):
        frq = defaultdict(int)
        cur_len = 0
        res = 0

        l = 0

        for r in range(len(nums)):
            frq[nums[r]] += 1

            while len(frq) > k:
                frq[nums[l]] -= 1
                if frq[nums[l]] == 0:
                    frq.pop(nums[l])
                l+=1
            
            res += r - l + 1
        
        return res



        