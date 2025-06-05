# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        res = []

        if count[0] % 2:
            return []
        
        for n in sorted(count):
            if count[n] > count[2 * n]:
                return []
            count[2 * n] -= count[n] if n else count[n] // 2

        for key, val in count.items():
            if val:
                res.extend([key] * val)
        return res

        
        