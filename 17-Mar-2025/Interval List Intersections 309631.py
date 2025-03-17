# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        result = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            st_a, end_a = firstList[i]
            st_b, end_b = secondList[j] 

            if max(st_a, st_b) <= min(end_a, end_b):
                result.append([max(st_a, st_b),min(end_a, end_b)])
            
            if end_a <= end_b:
                i+=1
            else:
                j+=1
        
        return result




            
        