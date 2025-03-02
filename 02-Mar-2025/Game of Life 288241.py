# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

from collections import defaultdict
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cell = defaultdict(int)

        for i in range(len(board)):
            for j in range(len(board[i])):
                count_live = 0
                count_dies = 0
                is_live = True if board[i][j] else False

                #top left 
                if j-1 >= 0 and i-1 >= 0:
                    if board[i-1][j-1]:
                        count_live+=1 
                    else:
                        count_dies+=1
                
                #top
                if i-1 >= 0:
                    if board[i-1][j]: 
                        count_live+=1
                    else:
                        count_dies+=1
                
                #top right
                if i-1 >= 0 and j+1 < len(board[i]):
                    if board[i-1][j+1]:
                        count_live+=1 
                    else:
                        count_dies+=1
                
                #left
                if j-1 >= 0:
                    if board[i][j-1]:
                        count_live+=1 
                    else: 
                        count_dies+=1
                
                #right 
                if j+1 < len(board[i]):
                    if board[i][j+1]:
                        count_live+=1 
                    else: 
                        count_dies+=1
                
                #bottom left
                if i+1 < len(board) and j-1 >= 0:
                    if board[i+1][j-1]:
                        count_live+=1 
                    else: 
                        count_dies+=1
                
                #bottom
                if i+1 < len(board):
                    if board[i+1][j]:
                        count_live+=1 
                    else: 
                        count_dies+=1
                
                #bottom right
                if i+1 < len(board) and j+1 < len(board[i]):
                    if board[i+1][j+1]:
                        count_live+=1 
                    else: 
                        count_dies+=1
                

                if is_live and (count_live < 2 or count_live > 3):
                    cell[f'{i}-{j}'] = 0  
                elif not is_live and count_live == 3:
                    cell[f'{i}-{j}'] = 1
        
        for key, val in cell.items():
            i,j = list(map(int, key.split('-')))
            board[i][j] = val

                    