# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #looking for levels
        #for every even level -> val's should be odd -> Increasing order (left to right)
        #for every odd level -> val's should be even -> Decreasing order (left to right)

        stack = []
        prev = {}
        stack.append((root, 0))

        while stack:
            node, depth = stack.pop()
            if node:
                is_even_depth = depth % 2 == 0
                is_even_value = node.val % 2 == 0

                if is_even_depth and not is_even_value:
                    if depth in prev and prev[depth] <= node.val:
                        return False
                    prev[depth] = node.val
                elif not is_even_depth and  is_even_value:
                    if depth in prev and prev[depth] >= node.val:
                        return False
                    prev[depth] = node.val
                else:
                    return False
                
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return True


        
        