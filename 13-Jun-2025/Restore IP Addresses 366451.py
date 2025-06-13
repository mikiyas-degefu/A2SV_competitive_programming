# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            if len(segment) > 3 or (len(segment) > 1 and segment[0] == '0'):
                return False
            value = int(segment)
            return 0 <= value <= 255

        def backtrack(start, current):
            if len(current) == 4:
                if start == len(s):
                    result.append('.'.join(current))
                return

            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        current.append(segment)
                        backtrack(start + length, current)
                        current.pop()

        result = []
        backtrack(0, [])
        return result