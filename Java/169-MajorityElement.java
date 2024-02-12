import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        // count<n, times it appears>
        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        int majorityCount = 0; 
        int majority = 0; 

        for (int i : nums){
            count.put(i, count.getOrDefault(i, 0) + 1);
        }

        for (int i: count.keySet()){
            if (count.get(i) > majorityCount){
                majority = i;
                majorityCount = count.get(i);
            } 
        }

        return majority;
    }
}