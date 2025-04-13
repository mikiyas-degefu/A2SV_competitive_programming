# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

from collections import defaultdict
class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        unique = defaultdict(int)

        for r in range(len(s)):
            if s[r] in unique:
                print(unique)
                result+=1
                unique.clear()
            
            unique[s[r]] += 1
        
        result += 1
        return result
            
        