# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def score(left, right):
            if left > right:
                return 0
            

            left_score = nums[left] - score(left + 1, right)
            right_score = nums[right] - score(left, right - 1)

            return max(left_score, right_score)
        

    
        return score(0, n - 1) >= 0
        