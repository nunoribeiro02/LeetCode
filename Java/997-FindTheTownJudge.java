import java.util.*;

class Solution {
    public int findJudge(int n, int[][] trust) {
        
        if (n == 1) return 1;
        List<Integer> judge = new ArrayList<Integer>();
        List<Integer> notJudge = new ArrayList<Integer>();

        for (int[] arr : trust){
            notJudge.add(arr[0]);

            if (!notJudge.contains(arr[1])) {
                judge.add(arr[1]);
            }

            
            if (judge.contains(arr[0])) {
                judge.removeIf(v -> v == arr[0]);
                notJudge.add(arr[0]);
            }
            
        }
        
        int[] judgeArr = judge.stream().mapToInt(Integer::intValue).toArray();   
        Set<Integer> judgeSet = new HashSet(judge);
        return ((judgeArr.length != n -1) || (judgeSet.size() != 1)) ? -1 : judgeArr[0];   
    }
}