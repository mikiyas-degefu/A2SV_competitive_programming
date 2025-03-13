# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        child = 0
        cookie = 0
        max_count = 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                max_count+=1
                child+=1
                cookie+=1
            elif g[child] < s[cookie]:
                child+=1
            elif  g[child] > s[cookie]:
                cookie+=1
            else:
                break
        
        return max_count

        