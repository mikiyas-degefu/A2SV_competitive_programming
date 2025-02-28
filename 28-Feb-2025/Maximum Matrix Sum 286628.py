# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        count_negative = 0
        sum_all = 0
        min_negative = float('inf')

        for i in matrix:
            for j in i:
                if j < 0:
                    count_negative+=1
                min_negative = min(min_negative, abs(j))
                sum_all+=abs(j)

        print(sum_all ,min_negative)
        if count_negative%2 != 0:
            return sum_all - (2 * min_negative)
        
        return sum_all
        