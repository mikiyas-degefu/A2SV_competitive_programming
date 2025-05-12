# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged = []

        for arr in matrix:
            merged.extend(arr)

        low = 0
        high = len(merged) - 1

        while low <= high:
            mid =( low + high) // 2

            if merged[mid] == target:
                return True
            elif merged[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
        