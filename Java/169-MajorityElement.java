import java.util.*;

/* 
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

Space: O(k), k is the number of distinct elements of the array
Time: O(n), n is the size of the array
*/

class Solution {
    public int majorityElement(int[] nums) {
        int majority = 0;
        int count = 0;

        for (int n : nums){
            // Reset majority candidate
            if (count == 0) {
                majority = n;
                count = 1;
            }
            else if (majority == n) count += 1;
            else if (majority != n) count -= 1;
        }

        return majority;
    }
}

/*
 Space: O(1)
 Time: O(n), n is the size of the array
 */