# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False  

class Solution:
    def longestWord(self, words: List[str]) -> str:

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True
        

        self.res = ""
        
        def dfs(node, path):
           
            if node != root and not node.end:
                return
            
            if len(path) > len(self.res) or (len(path) == len(self.res) and path < self.res):
                self.res = path
                
            for ch in sorted(node.children.keys()):
                dfs(node.children[ch], path + ch)
        
        dfs(root, "")
        return self.res
