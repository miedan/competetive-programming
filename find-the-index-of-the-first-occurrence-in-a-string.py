class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        j = 1
        
        lsp = [0 for i in range(len(needle))]

        while j < len(needle) :
         
            if needle[i] == needle[j]:
                
                lsp[j] = i + 1

                i += 1
                j += 1
                
            else:
                if i == 0:
                    j += 1
                else:
                    i = lsp[i-1]

                    



                

        i = 0
        j = 0

        while j < len(haystack):
            
            if haystack[j] == needle[i]:
               
                i += 1
                j += 1

               
            else:
                
                if i == 0:          
                    j += 1
                else:
                    i = lsp[i-1] 
            
            if i == len(needle):
                
                return j -  i


        return -1