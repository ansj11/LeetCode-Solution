class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                left = i
                break
        else:
            return [-1, -1]
        
        for i in range(n-1, -1, -1):
            if nums[i] == target:
                right = i
                break
        
        return [left, right]