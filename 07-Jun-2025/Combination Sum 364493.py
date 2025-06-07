# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(cur, path, start):
            if cur == target:
                res.append(path[:])
                return
            if cur > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                backtrack(cur + num, path, i)
                path.pop()

        backtrack(0, [], 0)
        return res