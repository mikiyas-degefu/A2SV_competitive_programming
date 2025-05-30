# Problem: Maximize the Confusion of an Exam - https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #sliding window for maximizing the T
        #sliding window for maximizing the F
        #return the max 

        left = 0
        cur_k = 0
        max_t = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'F':
                cur_k += 1

            while cur_k > k:
                if answerKey[left] == 'F':
                    cur_k -= 1
                left += 1

            max_t = max(max_t, right - left + 1)
        
        left = 0
        max_f = 0
        cur_k = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                cur_k += 1
        
            while cur_k > k:
                if answerKey[left] == 'T':
                    cur_k -= 1
                left += 1

            max_f = max(max_f, right - left + 1)
        
        return max(max_f, max_t)

