# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]

        current_po = 0

        while len(friends) > 1:
            current_po = (current_po + k - 1) % len(friends)
            friends.pop(current_po)
        
        return friends[0]

