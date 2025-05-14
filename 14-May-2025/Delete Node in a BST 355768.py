# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfsmin(node):
            cur = node
            while cur.left:
                cur = cur.left
            return cur

        def dfsDelete(node, key):
            if not node:
                return node
            
            if node.val < key:
                node.right = dfsDelete(node.right, key)
            elif node.val > key:
                node.left = dfsDelete(node.left, key)
            else:
                if not node.left:
                    return node.right
                
                if not node.right:
                    return node.left
                
                min_node = dfsmin(node.right)
                node.val = min_node.val

                node.right = dfsDelete(node.right, min_node.val)

            return node
        
        return dfsDelete(root, key)
        