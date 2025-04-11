# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [0]

        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        
        result = [-1] * len(nums)
        right = k
        x = (k * 2) + 1
        for right in range(k,len(nums) - k):
            total_sub = prefix[right + k + 1] - prefix[right - k]
            result[right] = total_sub // x
        
        return result
