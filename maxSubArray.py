class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = i+1
        s = sum(nums[i:j])
        while j<=len(nums):
            t = sum(nums[i:j])
            s = t if t>s else s
            if t>0:
                j += 1
            else:
                i = j
                j = i+1
        return s