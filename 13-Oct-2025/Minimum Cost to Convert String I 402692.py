# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = math.inf
        n = len(source)


        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0


        for o, c, z in zip(original, changed, cost):
            oi = ord(o) - ord('a')
            ci = ord(c) - ord('a')
            dist[oi][ci] = min(dist[oi][ci], z)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]


        total = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            si = ord(s_char) - ord('a')
            ti = ord(t_char) - ord('a')
            if dist[si][ti] == INF:
                return -1
            total += dist[si][ti]

        return int(total)
