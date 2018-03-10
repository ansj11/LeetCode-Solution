class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        '''
        x = 1
        y = 1
        i = 1
        while i<n:
            t = y
            y = x+y
            x = t
            i += 1
        return y