# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1

        for i in reversed(range(len(arr))):
            cur = arr[i]
            arr[i] = greatest
            if cur > greatest:
                greatest = cur
        
        return arr