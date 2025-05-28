# Problem: Three sum - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)-1):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
    
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

    
        return list(res)

