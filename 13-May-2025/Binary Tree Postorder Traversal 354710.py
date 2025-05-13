# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs_post_order(node):
            if node:
                dfs_post_order(node.left)
                dfs_post_order(node.right)
                res.append(node.val)
            return 
        
        dfs_post_order(root)
        return res


        