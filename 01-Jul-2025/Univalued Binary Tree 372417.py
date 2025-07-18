# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                if node.val != root.val:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        
        return True

        