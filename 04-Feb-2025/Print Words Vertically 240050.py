# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitted_word = s.split(" ")
        max_word_len = len(max(splitted_word, key=len))
        vertical_word = []

        for i,word in enumerate(splitted_word):
            if len(word) < max_word_len:
                space = max_word_len - len(word)
                space *= " " #add extra spacce 
                splitted_word[i]+=space
        
        for i in range(max_word_len):
            local_vertical_word = ''
            text_after_space = -1

            for index,word in enumerate(splitted_word):
                local_vertical_word+=word[i]
            
            if local_vertical_word is not '':
                vertical_word.append(local_vertical_word.rstrip()) 

        return vertical_word


        
        
            


        