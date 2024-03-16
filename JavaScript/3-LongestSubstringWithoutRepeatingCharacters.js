/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let subString = new Set();
    let left = 0; let right = 0;
    let longest = 0;
    for (c of s){
        while (subString.has(c)){
            subString.delete(s[left]);
            left++;
        }
        subString.add(c)
        right++;    
        longest = Math.max(longest, subString.size);
    }

    return longest;
};

// Time complexity: O(n)
// Space complexity: O(n)