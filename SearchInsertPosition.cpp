class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1, m;
        if (target <= nums[l])
            return l;
        else if (target > nums[r])
            return r + 1;
        else if (target == nums[r])
            return r;
        while (1){
            m = (l + r) / 2;
            if(nums[m] == target)
                return m;
            else if (nums[m] < target)
                l = m;
            else
                r = m;
            if (r-l == 1)
                return l+1;
        }
    }
};