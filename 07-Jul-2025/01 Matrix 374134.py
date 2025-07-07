# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        def in_bound(r,c):
            return 0 <= r < rows and 0 <= c < cols

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if in_bound(nr,nc) and mat[nr][nc] > mat[row][col] + 1:
                    mat[nr][nc] = mat[row][col] + 1
                    queue.append((nr, nc))
        return mat   


        