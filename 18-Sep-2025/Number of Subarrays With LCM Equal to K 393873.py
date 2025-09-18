# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            current_lcm = 1
            for j in range(i, n):
                if k % nums[j] != 0: 
                    break
                current_lcm = lcm(current_lcm, nums[j])
                if current_lcm == k:
                    count += 1
                elif current_lcm > k:
                    break
        return count

        