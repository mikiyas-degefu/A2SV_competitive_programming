# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

from collections import defaultdict, deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        min_stack = []
        min_dict = defaultdict(deque)
        n = len(nums)
        for i in range(2 * n):
            while min_stack and min_stack[-1] < nums[i % n]:
                min_dict[min_stack[-1]].append(nums[i % n])
                min_stack.pop()

            if i < n:
                min_stack.append(nums[i % n])
            
            while i >= n and min_stack and min_stack[-1] < nums[i % n]:
                min_dict[min_stack[-1]].append(nums[i % n])
                min_stack.pop()

        result = []
        for num in nums:
            if num in min_dict:
                result.append(min_dict[num].popleft())
            else:
                result.append(-1)

        return result