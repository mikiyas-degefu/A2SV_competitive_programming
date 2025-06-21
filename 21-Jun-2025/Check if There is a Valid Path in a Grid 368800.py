# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        left = {1 : {1,4,6}, 3 : {1,4,6}, 5 : {1,4,6}}
        right = {1 : {1,3,5}, 4 : {1,3,5}, 6 : {1,3,5}}
        up = {2 : {2,3,4}, 5 : {2,3,4}, 6 : {2,3,4}}
        down = {2 : {2,5,6}, 3 : {2,5,6}, 4 : {2,5,6}}
        visited = set()

        def is_bound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            visited.add((r,c))
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return True

            street = grid[r][c]
            
            # move down
            if street in down and is_bound(r + 1, c) and grid[r + 1][c] in down[street] and (r + 1, c) not in visited:
                if dfs(r + 1, c):
                    return True

            # move right
            if street in right and is_bound(r, c + 1) and grid[r][c + 1] in right[street] and (r, c + 1) not in visited:
                if dfs(r, c + 1):
                    return True

            # move up
            if street in up and is_bound(r - 1, c) and grid[r - 1][c] in up[street] and (r - 1, c) not in visited:
                if dfs(r - 1, c):
                    return True

            # move left
            if street in left and is_bound(r, c - 1) and grid[r][c - 1] in left[street] and (r, c - 1) not in visited:
                if dfs(r, c - 1):
                    return True

            return False
                    
        return dfs(0,0)