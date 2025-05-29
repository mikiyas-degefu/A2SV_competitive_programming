# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        left, cur_sum, res = 0, 0, 0

        for right in range(k):
            if s[right] in vowels:
                cur_sum += 1

        if cur_sum == k:
            return k
        
        res = max(cur_sum, res)
        for right in range(k, len(s)):
            res = max(cur_sum, res)
            if s[right] in vowels:
                cur_sum += 1
                
            if s[left] in vowels:
                cur_sum -= 1
        
            left += 1
        
        return max(cur_sum, res)


        