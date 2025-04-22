# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq_tracker = defaultdict(list)

        for idx, char in enumerate(s):
            frq_tracker[char].append(idx)
        
        for key, val in frq_tracker.items():
            if len(val) == 1:
                return val[0]
        
        return -1
        