# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name
        
        visited = set()
        result = []
    
        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)
        
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))
        
        return result