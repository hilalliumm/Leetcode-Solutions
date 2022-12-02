class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n<1: return False
        cvp=log(n,3)
        return abs(cvp-round(cvp))<1e-10
            