class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        num = digits[l]+1
        digits[l] = num%10
        res = num//10
        l -= 1
        while l>=0:
            num = digits[l]+res
            digits[l] = num%10
            res = num//10
            l -= 1
        if res!=0:
            digits.insert(0,1)
        return digits