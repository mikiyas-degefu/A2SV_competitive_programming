# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        in_degree = [0 for _ in range(n)]
        ans = [i for i in range(n)]
        queue = deque()

        #calculate the in degree
        for a, b in richer:
            graph[a].append(b)
            in_degree[b] += 1

        #find the richest 
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
            

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                in_degree[nei] -= 1

                #if the cur rich is less quite than nei
                if quiet[ans[node]] < quiet[ans[nei]]:
                     ans[nei] = ans[node]
                
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return ans
        