class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while(1):
            if (x/i)<i:
                return i-1
            i+=1