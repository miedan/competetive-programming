class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        
        
        i, j = 0, len(numbers) - 1
        arr = []

        while i < j:
            if numbers[i] + numbers[j] == target:
                arr.append(i + 1)
                arr.append(j + 1)
                return arr
            
            elif numbers[i] + numbers[j] > target:
                j -= 1

            else:
                
                i += 1

        return ans