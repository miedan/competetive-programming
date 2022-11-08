class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        ctr = Counter(changed)
        ans = []
        changed.sort()
        for num in changed:
            if num != 0 and ctr[num] > 0 and ctr[2 * num] > 0:
                ans.append(num)
                ctr[num] -= 1
                ctr[2 * num] -= 1
        ans.extend([0] * (ctr[0] // 2))
        if 2 * len(ans) != n:
            return []
        return ans