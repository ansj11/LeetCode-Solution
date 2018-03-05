class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if target <= nums[l]:
            return l
        if target == nums[r]:
            return r
        if target > nums[r]:
            return r+1
        while True:
            mid = (l + r) //2
            if nums[mid] ==target:
                return mid
            elif nums[mid] >target:
                r = mid
            else:
                l = mid
            if r-l <= 1:
                return l + 1