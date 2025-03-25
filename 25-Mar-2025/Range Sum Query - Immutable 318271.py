# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        cumulative = 0
        for num in nums:
            cumulative+=num
            self.prefix_sum.append(cumulative)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix_sum[right] -  self.prefix_sum[left - 1]
        else:
            return self.prefix_sum[right]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)