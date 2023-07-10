class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)

        def mergesort(left=0, right=n-1):
            if left >= right:
                return 0

            mid = (right + left) // 2
            left_count = mergesort(left, mid)
            right_count = mergesort(mid + 1, right)
            count = left_count + right_count

            index_i = left
            index_j = mid + 1
            
            while index_i <= mid and index_j <= right:
                if nums[index_i] <= 2 * nums[index_j]:
                    index_i += 1
                else:
                    count += mid + 1 - index_i
                    index_j += 1

            nums[left: right + 1] = sorted(nums[left: right + 1])

            return count

        return mergesort()