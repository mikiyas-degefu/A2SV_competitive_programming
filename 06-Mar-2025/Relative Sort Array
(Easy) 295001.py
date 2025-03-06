# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frq_count = defaultdict(int)
        not_arr2 = defaultdict(int)
        for num in arr2:
            frq_count[num] = 0
        
        for num in arr1:
            if num in frq_count:
                frq_count[num]+=1
            else:
                not_arr2[num]+=1
        
        result = []

        for num, frq in frq_count.items():
            result.extend([num] * frq)
        
        for num, frq in dict(sorted(not_arr2.items())).items():
            result.extend([num] * frq)
        

        return result
        


