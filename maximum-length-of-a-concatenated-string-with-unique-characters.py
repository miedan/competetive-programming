class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
       
        self.res = 0
        n = len(arr)

        def backtrack(arr,str_container):

            
            if len(str_container) != len(set(str_container)):
                return
            self.res = max(self.res, len(str_container))
            
                        
            for i in range(len(arr)):

                backtrack(arr[i+1:], str_container + arr[i])
                
                                              
        backtrack(arr, "")
        return self.res