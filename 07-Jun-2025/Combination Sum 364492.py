# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        N = len(candidates)

        def backtrack(cur, path):
            if cur == target:
                res.add(tuple(sorted(path)))
                return

            if cur > target:
                return
            

            for idx, num in enumerate(candidates):
                path.append(num)
                backtrack(cur + num, path)
                path.pop()

        
        backtrack(0, [])
        return list(res)
        