# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        result = [0] * len(indices)
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        
        return "".join(result)

        