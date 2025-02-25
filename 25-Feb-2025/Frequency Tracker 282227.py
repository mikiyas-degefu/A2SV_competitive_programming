# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.frq = defaultdict(int)          
        self.frq_tracker = defaultdict(int)  

    def add(self, number: int) -> None:
        current_freq = self.frq[number]
        
        if current_freq > 0:
            self.frq_tracker[current_freq] -= 1
            if self.frq_tracker[current_freq] == 0:
                del self.frq_tracker[current_freq]

        self.frq[number] += 1
        new_freq = self.frq[number]

        self.frq_tracker[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        if self.frq[number] == 0:
            return  

        current_freq = self.frq[number]

        self.frq_tracker[current_freq] -= 1
        if self.frq_tracker[current_freq] == 0:
            del self.frq_tracker[current_freq]

        self.frq[number] -= 1
        new_freq = self.frq[number]

        if new_freq > 0:
            self.frq_tracker[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frq_tracker.get(frequency, 0) > 0
