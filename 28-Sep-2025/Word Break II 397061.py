# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        memo = {}
        
        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            
            res = []
            node = trie.root
            
            for end in range(start, len(s)):
                ch = s[end]
                if ch not in node.children:
                    break
                node = node.children[ch]
                
                if node.is_word:
                    rest_sentences = dfs(end + 1)
                    word = s[start:end+1]
                    for sent in rest_sentences:
                        if sent:
                            res.append(word + " " + sent)
                        else:
                            res.append(word)
            
            memo[start] = res
            return res
        
        return dfs(0)
