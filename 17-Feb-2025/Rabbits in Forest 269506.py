# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        rabbits_response = defaultdict(int)

        for i in answers:
            rabbits_response[i]+=1

        result = 0
        for key, val in rabbits_response.items():
            if key == 0:
                result+=val
            elif val > (key + 1):
                if val % (key + 1) == 0:
                    result += (val // (key + 1) * (key + 1))
                else:
                    result += (val // (key + 1) * (key + 1)) + (key + 1)
            else:
                result+=(key + 1)

        return result