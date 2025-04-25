# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = []
        self.front = 0
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        diff = t - 3000
        while self.queue[self.front] < diff:
            self.front += 1
        
        return len(self.queue) - self.front
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)