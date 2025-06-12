# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def backtrack(node, cur_sum, path):
            if not node:
                return
            
            path.append(node.val)
            cur_sum += node.val

            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path[:])

            backtrack(node.left,cur_sum, path)
            backtrack(node.right,cur_sum, path)

            path.pop()


        backtrack(root,0,[])
        return res
        