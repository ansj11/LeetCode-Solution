class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int l = 0, r = height.size() - 1;
        
        while(l < r){
            int h = height[l] <= height[r] ? height[l] : height[r];
            int S = h * (r - l);
            maxArea = maxArea >= S ? maxArea : S;
            if (height[l] < height[r])
                l ++;
            else
                r --;
        }
        return maxArea;
    }
};