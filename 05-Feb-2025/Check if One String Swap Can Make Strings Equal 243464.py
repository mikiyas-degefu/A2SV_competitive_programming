# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        p1 = None
        p2 = None
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if p1 is None:
                    p1 = i
                elif p2 is None:
                    p2 = i
                else:
                    break

        if p1 is not None and p2 is not None:
            start = s2[:p1]
            middle = s2[p1+1:p2]
            last = s2[p2+1:]

            s2 = start+s2[p2]+middle+s2[p1]+last

        return True if s1 == s2 else False

        