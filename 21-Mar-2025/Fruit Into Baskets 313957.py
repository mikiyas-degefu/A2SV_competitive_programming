# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        two_boxs = defaultdict(int)
        left = 0
        right = 0
        max_elements = 0
        windows_sum = 0

        while right < len(fruits):
            if fruits[right] not in two_boxs and len(two_boxs) < 2:
                two_boxs[fruits[right]]+=1
                right+=1
                windows_sum+=1
                max_elements = max(max_elements, windows_sum)
            elif fruits[right] in two_boxs:
                two_boxs[fruits[right]]+=1
                right+=1  
                windows_sum+=1
                max_elements = max(max_elements, windows_sum)
            else:
                
                if  two_boxs[fruits[left]] == 1:
                    two_boxs.pop(fruits[left])
                else:
                    two_boxs[fruits[left]]-=1

                left+=1
                windows_sum = right - left

            
        return max_elements