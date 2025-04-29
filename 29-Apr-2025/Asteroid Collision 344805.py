# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:

            while stack and ast < 0 < stack[-1]:
                if -ast > stack[-1]:
                    stack.pop()
                    continue
                
                elif -ast == stack[-1]:
                    stack.pop()
                
                break
            else:
                stack.append(ast)
        
        return stack
        