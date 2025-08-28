# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n+1))  
        self.rank = [1] * (n+1)
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False  
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
