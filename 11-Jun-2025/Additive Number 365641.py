# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        sequence = []

        def backtrack(idx):
            if idx == n:
                return len(sequence) >= 3

            for i in range(idx, n):
                if num[idx] == '0' and i > idx:
                    break

                val = int(num[idx:i+1])

                if len(sequence) >= 2:
                    expected = sequence[-1] + sequence[-2]
                    if val < expected:
                        continue
                    elif val > expected:
                        break 

                sequence.append(val)
                if backtrack(i + 1):
                    return True
                sequence.pop()

            return False

        return backtrack(0)
