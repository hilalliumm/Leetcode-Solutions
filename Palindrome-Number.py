class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        result=0
        
        if x<0:
            return False
        else:
            while(temp!=0):
                result=result*10+temp%10
                temp=temp/10
               
        if(x==result):
           return True
        else:
           return False