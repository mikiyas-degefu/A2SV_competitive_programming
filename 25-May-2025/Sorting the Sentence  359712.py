# Problem: Sorting the Sentence  - https://leetcode.com/problems/sorting-the-sentence/description/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        result = [None] * len(words)

        for word in words:
            index = word[-1]

            result[int(index)-1] = word[:-1]

        return " ".join(result)
       


        