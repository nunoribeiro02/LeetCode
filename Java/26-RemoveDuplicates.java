class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int unique_i = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != nums[unique_i]){
                unique_i += 1;
                nums[unique_i] = nums[i];
            }
        }   
        return unique_i +1;
    }
}