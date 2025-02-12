# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = {}
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prd = nums[i] * nums[j]
                if prd in counter:
                    count += 8 * counter[prd]
                    counter[prd]+=1
                else:
                    counter[prd] = 1
        
        return count 

