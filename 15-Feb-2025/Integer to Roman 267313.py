# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        point = 1
        result = ''

        while(num > 0):
            n = (num % 10) * point
            num = num // 10
            point*=10
            roman = ''

            print(n)
            is_substract = False


            while(n > 0):
                if n >= 1 and n < 4:
                    roman+='I'
                    n = abs(n-1)
                elif n >= 4 and n < 9:
                    if n == 4:
                        is_substract = True
                    roman+='V'
                    n = abs(n-5)
                elif n >= 9 and n < 40 :
                    if n == 9:
                        is_substract = True
                    roman+='X'
                    n = abs(n-10)
                elif n >= 40 and n < 90:
                    if n == 40:
                        is_substract = True
                    roman+='L'
                    n = abs(n-50)
                elif n >= 90 and n < 400:
                    if n == 90:
                        is_substract = True
                    roman+='C'
                    n = abs(n-100)
                elif n >= 400 and n < 900:
                    if n == 400:
                        is_substract = True
                    roman+='D'
                    n = abs(n-500)
                else:
                    if n == 900:
                        is_substract = True
                    roman+='M'
                    n = abs(n-1000)
            
            roman = roman if not is_substract else roman[::-1]
            result = roman + result

        return result
