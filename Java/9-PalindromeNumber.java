class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        if (x < 0) {
            return false;
        }

        int right = str.length()-1;
        for (int left = 0; left <= right; left++){
            if (str.charAt(left) != str.charAt(right)){
                return false;
            }
            right--;
        }
        return true;
    }
}