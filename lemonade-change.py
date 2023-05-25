class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count = defaultdict(int)

        for i in bills:
            count[i] += 1

            if i == 10:

                if count[5] >= 1:
                    count[5] -=1
                else:
                    return False

            elif i == 20:

                if count[5] >=1 and count[10] >= 1:
                    count[5] -= 1
                    count[10] -= 1

                elif count[5] > 2:
                    
                    count[5] -= 3
                else:
                    return False
                   
        return True