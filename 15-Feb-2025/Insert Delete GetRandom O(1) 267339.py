# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random
class RandomizedSet:

    def __init__(self):
        self.val = set()
        self.data = []
        

    def insert(self, val: int) -> bool:
        if val in self.val:
            return False
        self.val.add(val)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.val:
            self.val.remove(val)
            self.data.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data) - 1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()