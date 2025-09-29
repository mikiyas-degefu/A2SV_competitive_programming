# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.freq = 0

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        root = TrieNode()
        for word, freq in count.items():
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
            node.freq = freq
        
        result = []
        def dfs(node):
            if node.word:
                result.append((node.word, node.freq))
            for ch in sorted(node.children.keys()):  
                dfs(node.children[ch])
        
        dfs(root)
        
        result.sort(key=lambda x: (-x[1], x[0]))
        
        return [word for word, _ in result[:k]]