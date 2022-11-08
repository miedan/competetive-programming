class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        k = []
         
        for idx in range(x):
            maximum = max(arr[:x - idx])
            max_idx = arr.index(maximum) + 1
            arr[:max_idx] = reversed(arr[:max_idx])
            k.append(max_idx)
            arr[:x - idx] = reversed(arr[:x - idx])
            k.append(x - idx)
        return k
        