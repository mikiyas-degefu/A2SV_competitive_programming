# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0 for i in range(numCourses)]
        res = []
        queue = deque()


        for cur, pre in prerequisites:
            graph[pre].append(cur)
            in_degree[cur] += 1
        
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            res.append(course)

            for nei in graph[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        if len(res) != numCourses:
            return []
        return res

