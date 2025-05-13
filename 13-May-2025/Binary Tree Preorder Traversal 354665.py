# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def def_pre_order(node):
            if node:
                result.append(node.val)
                def_pre_order(node.left)
                def_pre_order(node.right)
            return
        
        def_pre_order(root)
        return result
        