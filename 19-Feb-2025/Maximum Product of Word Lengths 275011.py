# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_size = 0
        for i in range(len(words)):
            word_1 = set(words[i])

            for j in range(i+1, len(words)):
                word_2 = set(words[j])

                if not(word_1 & word_2):
                    product = len(words[i]) * len(words[j])
                    if max_size <= product:
                        max_size = product
        
        return max_size
        