class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        Arrays.sort(piles);
        int r = piles[piles.length-1];
        int k = r;

        while (l <= r){
            int m = (int) Math.floor( (l + r) / 2);
            int time = 0;
            for (int banana : piles){
               time += Math.ceil((double)  banana / m);
               if (time > h){
                   break;
               }
            }

            if (time > h){
                l = m +1;
            }
            else{
                k = Math.min(m, k);
                r = m -1;
            }
        }

        return k;
    }
}

// Time: O(nlogn)
// Space: O(1)