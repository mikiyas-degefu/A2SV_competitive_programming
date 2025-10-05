# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_prefix = False  

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

                node.is_prefix = True

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue 

            node = root
            j = i

            while j < n and target[j] in node.children:
                node = node.children[target[j]]
                j += 1
                if node.is_prefix:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != float('inf') else -1
