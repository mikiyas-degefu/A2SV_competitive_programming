# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.string_ids = set()

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        root = TrieNode()
        
        def insert(word: str, idx: int):
            for i in range(len(word)):
                node = root
                for j in range(i, len(word)):
                    ch = word[j]
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                    node.string_ids.add(idx)
        
        n = len(arr)
        for i, word in enumerate(arr):
            insert(word, i)
        
        answer = []
        

        for i, word in enumerate(arr):
            candidate = None
            for length in range(1, len(word) + 1):  
                substrings = []
                for start in range(len(word) - length + 1):
                    sub = word[start:start+length]
                    

                    node = root
                    for ch in sub:
                        node = node.children[ch]
                    if node.string_ids == {i}:  #
                        substrings.append(sub)
                
                if substrings:
                    candidate = min(substrings)  
                    break
            
            answer.append(candidate if candidate else "")
        
        return answer
