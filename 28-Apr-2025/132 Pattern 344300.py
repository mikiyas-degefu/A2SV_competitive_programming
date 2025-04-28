# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []
        cur_min = nums[0]

        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack  and num > stack[-1][1]:
                return True
            
            stack.append([num, cur_min])
            cur_min = min(cur_min, num)

        

        return False

        