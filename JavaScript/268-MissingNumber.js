/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort(((a,b) => a- b));
    let i = 0;
    for (let n of nums){
        if (i != n) break;
        
        i += 1;
    }
    return i;
};

/*
Space: O(1)
Time: O(n)
*/
