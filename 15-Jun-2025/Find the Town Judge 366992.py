# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)

        for i,j in trust:
            count[i] -= 1
            count[j] += 1

        
        for i in range(1,n + 1):
            if count[i] == n - 1:
                return i
            
        return -1
        