# Problem: Maximum XOR With an Element From Array - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/

class TrieNode:
    def __init__(self):
        self.child = [None, None]

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        q = [(x, m, i) for i, (x, m) in enumerate(queries)]
        q.sort(key=lambda x: x[1])  
        
        res = [-1] * len(queries)
        root = TrieNode()
        idx = 0
        n = len(nums)
        
        def insert(num):
            node = root
            for bit in range(31, -1, -1):  
                b = (num >> bit) & 1
                if not node.child[b]:
                    node.child[b] = TrieNode()
                node = node.child[b]
        
        def maxXor(x):
            node = root
            if not node.child[0] and not node.child[1]:
                return -1
            ans = 0
            for bit in range(31, -1, -1):
                b = (x >> bit) & 1
                
                if node.child[1 - b]:
                    ans |= (1 << bit)
                    node = node.child[1 - b]
                else:
                    node = node.child[b]
            return ans
        
        for x, m, i in q:
            while idx < n and nums[idx] <= m:
                insert(nums[idx])
                idx += 1
            res[i] = maxXor(x)
        
        return res
