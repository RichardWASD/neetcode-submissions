class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        What is a square root? 
        a number that multiplies its self to give us the product of that production

        : sqrt is finding a number that multiplies itself to get said number 
        '''

        l,r = 0, x;

        while (l <= r):
            m = (l+r) // 2 ;

            if(m*m == x ):
                return m;
            elif(m*m > x):
                r = m-1;
            else:
                l = m+1;
        return r;
        