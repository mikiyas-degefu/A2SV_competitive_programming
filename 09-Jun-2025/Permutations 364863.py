# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        visited = set()
        res = []

        def backtrack():
            if len(stack) == len(nums):
                res.append(stack[:])
                return 

            for i,num in enumerate(nums):
                if i not in visited:
                    stack.append(num)
                    visited.add(i)
                    backtrack()
                    stack.pop()
                    visited.remove(i)
        
        backtrack()
        return res
        