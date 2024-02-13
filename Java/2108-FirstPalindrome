class Solution {
    public String firstPalindrome(String[] words) {
        String palindrome = "";
        for (String w: words){
            if (findPalindrome(w)){
                palindrome = w;
                break;
            }
        }

        return palindrome;
    }

    public boolean findPalindrome(String word){
        int i = 0, j = word.length()-1;

        while (i <= j){
            if (word.charAt(i) == word.charAt(j)){
                i++;
                j--;
            }
            else return false;
        }

        return true;
    }
}

/* Notes: Second function was not necessary, could just check if 'word' reversed is equal to 'word'
 Space: O(1)
 Time: O(n * m), n the size of vector and m the longest string
 */