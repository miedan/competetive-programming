class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)
        arr, output = [], []
        for i in count:
            arr.append((-(count[i]), i))
        
        heapify(arr)

        while k:

            p = (heappop(arr))
            output.append(p[1])
            k -= 1
        return output