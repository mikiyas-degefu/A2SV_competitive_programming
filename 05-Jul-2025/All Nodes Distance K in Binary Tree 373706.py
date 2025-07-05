# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if node:
                if parent:
                    graph[node].append(parent)
                    graph[parent].append(node)
                build_graph(node.left, node)
                build_graph(node.right, node)
        
        build_graph(root, None)

        visited = set()
        queue = deque()
        queue.append((target, 0))
        visited.add(target)
        result = []

        while queue:
            node, level = queue.popleft()
            if level == k:
                result.append(node.val)
            elif level < k:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        return result



        
        