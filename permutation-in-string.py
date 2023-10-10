class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        check = defaultdict(int)
        dic = defaultdict(int)

        flag = False

        if len(s1) > len(s2):
            return False

        for i in s1:
            dic[i] += 1
        # print(dic)

        for i in range(len(s1)):
            check[s2[i]] += 1
        f = False
        for i in check:
            if i not in dic or dic[i] != check[i]:
                f = True

        if not f:
            return True
            
                

        # print(check)

        left = 0
        l = len(s1)

        for right in range(l,len(s2)):
            flag = False

            check[s2[left]] -= 1
            check[s2[right]] += 1

            if check[s2[left]] == 0:
                del check[s2[left]]
            
            for i in check:
                if i not in dic or dic[i] != check[i]:
                    flag = True
                    break

            if not flag:
                return True

            left += 1

            

        return False