# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        cur_sum = sum(cardPoints[:n - k])
        
        res = total_sum - cur_sum
        left = 0
        right = n - k
        while right < n:
            res = max(res, total_sum - cur_sum)
            cur_sum -= cardPoints[left]
            cur_sum += cardPoints[right]
            left += 1
            right += 1
        
        res = max(res, total_sum - cur_sum)
        return res


