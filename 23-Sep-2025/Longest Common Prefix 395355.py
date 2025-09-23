# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def longest_common_prefix(self) -> str:
        prefix = ""
        node = self.root
        while node and not node.is_end and len(node.children) == 1:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.longest_common_prefix()