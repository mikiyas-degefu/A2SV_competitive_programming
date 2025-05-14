# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def mergeTree(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            
            node1.val += node2.val
            node1.left = mergeTree(node1.left, node2.left)
            node1.right = mergeTree(node1.right, node2.right)

            return node1
        
        return mergeTree(root1, root2)
            

        