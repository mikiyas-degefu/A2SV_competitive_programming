# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0

        heap = [(0, k)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            if curr_dist > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_dist = max(distances.values())
        return max_dist if max_dist != float('inf') else -1