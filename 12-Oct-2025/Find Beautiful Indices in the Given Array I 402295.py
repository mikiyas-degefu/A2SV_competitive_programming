# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        a_indices = []
        b_indices = []
        la, lb = len(a), len(b)

        for i in range(len(s) - la + 1):
            if s[i:i+la] == a:
                a_indices.append(i)
        for j in range(len(s) - lb + 1):
            if s[j:j+lb] == b:
                b_indices.append(j)


        result = []
        for i in a_indices:
            
            left = bisect_left(b_indices, i - k)
            right = bisect_right(b_indices, i + k)
            if left < right:  
                result.append(i)

        return result
