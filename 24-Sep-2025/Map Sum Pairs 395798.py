# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0 


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_map = {} 

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_map.get(key, 0)
        self.key_map[key] = val

        node = self.root
        node.score += delta
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.score += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.score
