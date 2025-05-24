# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_of_letter = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        def backtrack(idx, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return 
            
            for c in digits_of_letter[digits[idx]]:
                backtrack(idx + 1, curStr + c)

        res = []
        if digits:
            backtrack(0, "")
        return res