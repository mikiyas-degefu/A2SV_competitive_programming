# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        result = []
        even_sum = [x for x in nums if x % 2 == 0]
        even_sum = sum(even_sum)

        for i,j in queries:
            if nums[j] % 2 == 0:
                even_sum -= nums[j]
            nums[j]+=i

            if nums[j] % 2 == 0:
                even_sum += nums[j]
                
            result.append(even_sum)

        return result


