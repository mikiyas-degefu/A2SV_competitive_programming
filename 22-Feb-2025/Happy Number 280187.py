# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        num_lists = set()
        
        product = n
        while True:
            number = str(product)
            pr = 0
            for num in number:
                pr += int(num)**2
            
            if pr in num_lists:
                return False
            if pr == 1:
                return True

            num_lists.add(pr)
            product = pr
        
            


