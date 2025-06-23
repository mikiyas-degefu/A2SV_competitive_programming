# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()  # recursion stack
        checked = set()  # fully processed nodes

        for main, pre in prerequisites:
            preMap[pre].append(main)
        
        def dfs(course):
            if course in checked:
                return True  # already processed, no cycle here
            if course in visited:
                return False  # cycle detected
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): 
                    return False
            visited.remove(course)
            checked.add(course)  # mark as fully processed
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
