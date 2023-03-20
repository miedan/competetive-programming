class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr) - 1
        for i in range(n):
            if (arr[i-1] < arr[i]) and (arr[i] > arr[i+1]):
                ans = i

        return ans