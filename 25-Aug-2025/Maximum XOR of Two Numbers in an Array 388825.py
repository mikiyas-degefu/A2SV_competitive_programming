# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = {}
        
        for num in nums:
            node = trie
            for i in range(31, -1, -1): 
                bit = (num >> i) & 1
                node = node.setdefault(bit, {})

        max_xor = 0
        for num in nums:
            node = trie
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opp = 1 - bit
                if opp in node:  
                    curr_xor |= (1 << i)
                    node = node[opp]
                else:
                    node = node[bit]
            max_xor = max(max_xor, curr_xor)
        
        return max_xor
