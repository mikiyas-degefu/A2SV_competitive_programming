# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True
        
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]

            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word:
                    dp[i] = min(dp[i], dp[j + 1])
        
        return dp[0]
