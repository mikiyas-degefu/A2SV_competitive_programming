# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_w = float('inf')
        left = 0
        right = 0

        min_window = 0

        while right < k:
            if blocks[right] == 'W':
                min_window+=1
            right+=1
        
        min_w = min(min_w, min_window)

        while right < len(blocks):
            if blocks[left] == 'W' and blocks[right] == 'B':
                min_window-=1
            elif blocks[left] == 'B' and blocks[right] == 'W':
                min_window+=1

            right+=1
            left+=1
            min_w = min(min_w, min_window)
        

        return min_w if min_w > 0 else 0