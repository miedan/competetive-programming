class Solution:
    def longestPrefix(self, s: str) -> str:
                  
        i = 0
        j = 1
        
        
        lsp = [0 for _ in range(len(s))]
      

        while j < len(s) :
         
            if s[i] == s[j]:
                # print(i,j)
                lsp[j] = i + 1

               

                i += 1
                j += 1
                
                
            else:
                
                
                if i == 0:
                    j += 1

                else:
                    i = lsp[i-1]
                    

        return s[:lsp[len(s)-1]]