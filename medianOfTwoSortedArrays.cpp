class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> v;
        int len1 = nums1.size();
        int len2 = nums2.size();

        int i = 0, j = 0;
        while (i<len1||j<len2)
        {
            if (i<len1&&j<len2)
            {
                if (nums1[i] <= nums2[j])
                {
                    v.push_back(nums1[i]);
                    i++;
                }
                else
                {
                    v.push_back(nums2[j]);
                    j ++;
                }
            }
            else if (i == len1&&j < len2)
            {
                v.push_back(nums2[j]);
                j++;
            }
            else
            {
                v.push_back(nums1[i]);
                i++;
            }
        }
        if ((len1 + len2) % 2 == 0)
            return (v[(len1 + len2) / 2] + v[(len1 + len2) / 2 - 1]) / 2.0;
        else
            return v[(len1 + len2) / 2];
    }
};