# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        stack = []
        path = set()

        def backtrack():
            if len(stack) == len(nums):
                res.add(tuple(stack[:]))
                return
            
            for i, num in enumerate(nums):
                if i not in path:
                    stack.append(num)
                    path.add(i)
                    backtrack()
                    path.remove(i)
                    stack.pop()
        backtrack()
        return list(res)
        