# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        result = '' 

        for i in range(len(s)):
            l,r = i, i
            #odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    result = s[l:r+1]
                    res_len = r - l + 1
                l-=1
                r+=1
            
            #even
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    result = s[l:r+1]
                    res_len = r - l + 1
                l-=1
                r+=1
        
        return result
