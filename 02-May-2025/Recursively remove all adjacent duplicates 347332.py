# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

class Solution:
    def removeUtil(self, S):
        n = len(S)
        
        if n <= 1:
            return S
        
        result = ''
        i = 0
        while i < n:
            if i < n-1 and S[i] == S[i+1]:
                while i < n-1 and S[i] == S[i+1]:
                    i += 1
                i += 1 
            else:
                result += S[i]
                i += 1

 
        if len(result) == n:
            return result
    
        return self.removeUtil(result)