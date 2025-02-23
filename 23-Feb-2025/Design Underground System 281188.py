# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(list)
        self.total_time_station = defaultdict(lambda: [0, 0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check = self.check_in[id]
        time_diff = t  - check[1]
        self.total_time_station[f'${check[0]}-${stationName}'][0]+=time_diff
        self.total_time_station[f'${check[0]}-${stationName}'][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg_time = self.total_time_station[f'${startStation}-${endStation}']
        return avg_time[0] / avg_time[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)