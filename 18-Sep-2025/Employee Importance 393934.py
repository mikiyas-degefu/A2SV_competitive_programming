# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        total = 0
        queue = deque([id])
        
        while queue:
            emp_id = queue.popleft()
            employee = emp_map[emp_id]
            total += employee.importance
            queue.extend(employee.subordinates)
        
        return total