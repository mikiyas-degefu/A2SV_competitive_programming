# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)
        
        def is_subsequence(word: str) -> bool:
            prev = -1
            for ch in word:
                if ch not in pos:
                    return False
                idx_list = pos[ch]
                idx = bisect.bisect_right(idx_list, prev)
                if idx == len(idx_list):  
                    return False
                prev = idx_list[idx]
            return True
        
        count = 0
        for w in words:
            if is_subsequence(w):
                count += 1
        return count
