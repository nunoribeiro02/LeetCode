/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let i = 0;
    let j = numbers.length -1;

    while (i < j){
        let sum = numbers[i] + numbers[j];
        if (sum == target){
            return [i +1, j+1];
        }
        else if (sum < target) i++;
        else if (sum > target) j--;
    }
};

/*
Space: O(1)
Time: O(n)
*/