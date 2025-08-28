# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n   
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union_set(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
           
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        numberOfComponents = n
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    if dsu.find(i) != dsu.find(j):
                        dsu.union_set(i, j)
                        numberOfComponents -= 1
        
        return numberOfComponents
