class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        num_counts = []
        for num, count in Counter(arr).items():
            num_counts.append((num, count))
        num_counts.sort(key=lambda x: x[1], reverse=True)

        t_count = 0
        for i in range(len(num_counts)):
            (num, count) = num_counts[i]
            t_count += count
            if t_count >= len(arr) // 2:
                return i + 1


        