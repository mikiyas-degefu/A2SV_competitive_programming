# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row =  'zxcvbnm'

        result = []

        for word in words:
            row_one = 0
            row_two = 0
            row_three = 0
 
            for char in word.lower():  

                if char in first_row:
                    row_one+=1
                elif char in second_row:
                    row_two +=1
                else:
                    row_three+=1

            if len(word) == row_one or len(word) == row_two or len(word) == row_three:
                result.append(word)

        
        return result
                
            
                    



        