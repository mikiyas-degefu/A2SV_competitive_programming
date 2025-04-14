# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)

        result = 0
        size = skill[0] + skill[n - 1]

        l = 0
        r = n - 1

        while l < r:
            result += skill[l] * skill[r]
            if skill[l] + skill[r] != size:
                return -1
            l += 1
            r -=1
        
        return result
