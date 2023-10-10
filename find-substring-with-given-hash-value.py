class Solution:
    def subStrHash(self, s: str, power: int,m: int, k: int, hashValue: int) -> str:
    
        cur_hash = 0
        c = k - 1
        r = len(s)- k - 1
        start_index = 0
        second_index = 0
        
        
        for i in range(len(s)-1, r,-1):
            ch = s[i]
      
            cur_hash += ((ord(ch)-96) * pow( power , c,m))
            c -= 1
            cur_hash %= m
        # print(cur_hash)

        if cur_hash % m == hashValue:

            # print("hey")
            # print(len(s)-1)
            start_index = r+1
            second_index = len(s)
        
            
            # return s[r+1:(len(s))]


        left = len(s) -1
        c = k - 1
        
        for right in range(r,-1,-1):
       

            left_hash = ((ord(s[left]) - 96) )
           
            cur_hash -= (left_hash * pow( power,c,m))
            cur_hash *= power
            cur_hash += ((ord(s[right]) - 96))

            if (cur_hash % m) == hashValue:
                
                start_index = right
                second_index = left
                
            cur_hash%=m

            left -= 1
        return s[start_index:second_index]