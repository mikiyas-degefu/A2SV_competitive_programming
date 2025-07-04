# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        answer = [-1 for i in range(n)]

        for a,b in redEdges:
            red_graph[a].append(b)

        for u,v in blueEdges:
            blue_graph[u].append(v)
        
        queue = deque()
        queue.append([0, 0, None]) #node, length, prev color 
        visited = set()
        visited.add((0,None)) #node and prev color

        #bfs
        while queue:
            node,length, edgeColor =  queue.popleft()

            if answer[node] == -1:
                answer[node] = length
            
            if edgeColor != 'red':
                for nei in red_graph[node]:
                    if (nei, 'red') not in visited:
                        visited.add((nei, 'red'))
                        queue.append([nei,length + 1, 'red']) 
            
            if edgeColor != 'blue':
                for nei in blue_graph[node]:
                    if (nei, 'blue') not in visited:
                        visited.add((nei, 'blue'))
                        queue.append([nei,length + 1, 'blue']) 
        
        return answer

        
        
        