class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while True:
            if r*r > x:
                r = (r + x//r) // 2
            else: 
                return int(r)