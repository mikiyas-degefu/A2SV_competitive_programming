# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        for current_box in range(len(boxes)):
            if boxes[current_box] == "1":
                for new_position in range(len(boxes)):
                    answer[new_position] += abs(new_position - current_box)
        return answer