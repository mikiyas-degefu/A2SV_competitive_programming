# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0

        for word in words:
            temp_chars = chars
            can_generated = True
            for char in word:
                if char in temp_chars:
                    temp_chars = temp_chars.replace(char, '', 1)
                else:
                    can_generated = False
                    break

            if can_generated:
                count+=len(word)
        
        return count



