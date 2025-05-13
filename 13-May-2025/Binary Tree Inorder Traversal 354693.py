# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs_in_order(node):
            if node:
                dfs_in_order(node.left)
                res.append(node.val)
                dfs_in_order(node.right)

        dfs_in_order(root)
        return res
        