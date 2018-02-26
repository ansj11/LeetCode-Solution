class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >nums[r]:
                l = mid + 1
            else:
                r = mid
        
        res = l
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) //2
            realmid = (mid + res) % n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1