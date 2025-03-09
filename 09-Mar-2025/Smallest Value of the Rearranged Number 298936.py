# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = True if num < 0 else False

        if is_negative:
            num *= -1

        nums = list(map(int, list(str(num))))

        if not is_negative:
            nums.sort()
            min_num = min(nums, key=lambda x : float('inf') if x == 0 else x )
            nums.remove(min_num)
            return (int(str(min_num)+"".join(map(str, nums))))
        
        nums.sort(reverse = True)
        max_num = max(nums)
        nums.remove(max_num)
        return -1 * (int(str(max_num)+"".join(map(str, nums))))

        