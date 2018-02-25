class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = []
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        while i < len1 or j < len2:
            if i < len1 and j < len2:
                if nums1[i] <= nums2[j]:
                    lst.append(nums1[i])
                    i += 1
                else:
                    lst.append(nums2[j])
                    j += 1
            elif i == len1 and j < len2:
                lst.append(nums2[j])
                j += 1
            else:
                lst.append(nums1[i])
                i += 1
        length = len1 + len2
        if length % 2 == 0:
            return (lst[length // 2 - 1] + lst[length // 2]) / 2.0
        else:
            return lst[length // 2]