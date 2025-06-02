class Solution {
    public int findMin(int[] nums) {
        int res = nums[0];
        int l = 0;
        int r = nums.length -1;
        int m;
        while (l <= r){
            if (nums[l] < nums[r]){
                if (nums[l] < res){
                    res = nums[l];
                }
                return res;
            }

            m = (l + r) / 2;
            if (nums[m] < res){
                res = nums[m];
            }

            if (nums[m] >= nums[l]){
                l = m +1;
            } 
            else{
                r = m -1;
            }
        }
        return res;
    }
}