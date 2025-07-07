# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        queue = deque([(entrance[0], entrance[1], 0)])
        visited.add((entrance[0], entrance[1]))

        def in_bound(r,c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])

        while queue:
            cur_row, cur_col, level = queue.popleft()
        
            for dr, dc in dirs:
                nr = cur_row + dr
                nc = cur_col + dc

                if in_bound(nr,nc) and (nr, nc) not in visited and maze[nr][nc] == '.':
                    if nr == 0 or nr == len(maze) - 1 or nc == 0 or nc == len(maze[0]) - 1:
                        return level + 1
                    queue.append([nr,nc, level+1])
                    visited.add((nr,nc))
        
        return -1
        



        