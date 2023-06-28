class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        n = len(skill)
        team = n / 2

        pairsum = sum(skill) % team 

        if pairsum != 0:
            return -1

        ans = 0
        skill.sort()

        left = 0
        right = n-1
        res = skill[left] + skill[right]
        while left <= right:
            if res != skill[left] + skill[right]:
                return -1
            else:
                ans += skill[left] * skill[right]
                left += 1
                right -= 1
        return ans