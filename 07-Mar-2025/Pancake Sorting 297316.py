# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flip_result = []
        l = len(arr) 

        while l != 0:
            mx = arr.index(max(arr[:l]))
            arr = arr[:mx+1][::-1] + arr[mx+1::]
            arr = arr[:l][::-1]+arr[l:]
            flip_result.append(mx+1)
            flip_result.append(l)
            l-=1
        return flip_result
    