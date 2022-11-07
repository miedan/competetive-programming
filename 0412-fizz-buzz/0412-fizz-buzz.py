class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        o=[]
        for i in range (1,n+1):
            if i%15==0:
                o.append("FizzBuzz")
            elif i%3==0:
                o.append("Fizz")
            elif i%5==0:
                o.append("Buzz")
            else:
                i=str(i)
                o.append(i)
        return (o)
    
        