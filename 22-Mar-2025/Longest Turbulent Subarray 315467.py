# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1
        left = 0
        right = 0
        win_max = 1
        flag = True
        
        while right < len(arr) - 1:
            if (flag and arr[right] > arr[right + 1]) or (not flag and arr[right] < arr[right + 1]):
                win_max+=1
                flag = not flag
                right+=1
            else:
                max_len = max(max_len, ((right - left) + 1))
                flag = not flag 
                if arr[right] == arr[right + 1]:
                    right+=1
                left = right
        
        max_len = max(max_len, ((right - left) + 1))
        return max_len

