# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        traverse_key = defaultdict(list)
        result = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                traverse_key[i+j].append(mat[i][j])

        
        is_up = False
        for key, val in traverse_key.items():
            if is_up:
                result.extend(val)
            else:
                val.reverse()
                result.extend(val)
            
            is_up = not is_up
        
        return result

        
        
                