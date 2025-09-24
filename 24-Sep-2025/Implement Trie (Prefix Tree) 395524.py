# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TriesNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root = TriesNode()
        
    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not cur.children[idx]:
                cur.children[idx] = TriesNode()
    
            cur = cur.children[idx]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not cur.children[idx]:
                return False
            
            cur = cur.children[idx]
        
        return cur.is_end
            
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)