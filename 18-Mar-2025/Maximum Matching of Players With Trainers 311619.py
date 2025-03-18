# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        max_match = 0

        i = 0
        j = 0 

        while i < len(players) and j < len(trainers):
            if players[i] > trainers[j]:
                j+=1
            else:
                i+=1
                max_match+=1
                j+=1
        
        return max_match
        