# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(pow(2,len(nums))):
            cur = []
            for j in range(len(nums)):
                if i & (1 << j):
                    cur.append(nums[j])
            res.append(cur)
        
        return res