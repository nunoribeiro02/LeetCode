class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> prevNums = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int val = target - nums[i];

            if (prevNums.containsKey(val)){
                return new int[]{i, prevNums.get(val)};
            }
            else{
                prevNums.put(nums[i], i);
            }
        }

        return new int[]{-1, -1};
    }
}