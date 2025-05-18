# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = str(root.val)
        if root.left or root.right:
            s += "(" + self.tree2str(root.left) + ")"
        if root.right:
            s += "(" + self.tree2str(root.right) + ")"
        return s