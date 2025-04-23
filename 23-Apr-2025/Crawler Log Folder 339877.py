# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for d in logs:
            if d == "../":
                if stack:
                    stack.pop()
            elif d == "./":
                continue
            else:
                stack.append(d)
        return len(stack)