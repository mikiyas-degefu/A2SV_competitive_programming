# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        queue = deque([0])
        keys = set([0])
        while queue:
            node = queue.popleft()

            for key in rooms[node]:
                if key not in keys:
                    keys.add(key)
                    queue.append(key)
                    
        return len(keys) == len(rooms)



        