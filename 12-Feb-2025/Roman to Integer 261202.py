# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        result = 0
        prev = ''

        for i in s[::-1]:
            if result <= roman_nums[i] or prev == roman_nums[i]  :
                result+=roman_nums[i]
                prev = roman_nums[i]
            else:
                result-=roman_nums[i]
        
        return result



        