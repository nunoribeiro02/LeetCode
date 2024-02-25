import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<>();
        int[] res = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++){
            res[i] = 0;
            int t = temperatures[i];
            if (stack.isEmpty()){
                stack.push(new int[]{t, i});
                continue;
            }
            
            while (!stack.isEmpty() && t > stack.peek()[0]){
                int prevIndex = stack.pop()[1];
                res[prevIndex] = i - prevIndex;            
            }
            stack.push(new int[]{t, i});
        }

        return res;
    }
}

/*
 Space: O(2n) = O(n), n is the size of the array
 Time: O(n), n is the size of the array
*/